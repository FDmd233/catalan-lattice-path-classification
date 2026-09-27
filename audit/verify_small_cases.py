#!/usr/bin/env python3
"""Exact low-dimensional checks for the Catalan-classification manuscript.

These computations are not used in the proof.  They are regression checks for
several local lemmas and for the final classification in dimensions n <= 4.
Only the Python standard library is required.
"""

from itertools import combinations, product


def wt(x):
    return sum(x)


def words(n):
    return list(product((0, 1), repeat=n))


def B(x, y):
    sx = sy = ans = 0
    for a, b in zip(x, y):
        if a == b and sx == sy:
            ans ^= 1
        sx += a
        sy += b
    return ans


def dyck_prefixes(n):
    out = []
    for p in product((1, -1), repeat=n):
        h = 0
        ok = True
        for a in p:
            h += a
            if h < 0:
                ok = False
                break
        if ok:
            out.append(p)
    return out


def dyck_words(n):
    return [p for p in dyck_prefixes(2 * n) if sum(p) == 0]


def matching(P):
    stack = []
    edges = []
    for i, a in enumerate(P):
        if a == 1:
            stack.append(i)
        else:
            edges.append((stack.pop(), i))
    return tuple(edges), tuple(stack)


def blocks(P):
    edges, unmatched = matching(P)
    out = {}
    for x in words(len(P)):
        if all(x[a] != x[b] for a, b in edges):
            label = tuple(x[i] for i in unmatched)
            out.setdefault(label, []).append(x)
    return out


def check_recurrence(max_d=8):
    for d in range(1, max_d + 1):
        for p in words(d - 1):
            for q in words(d - 1):
                for a in (0, 1):
                    for b in (0, 1):
                        lhs = B(p + (a,), q + (b,))
                        rhs = B(p, q) ^ int(a == b and wt(p) == wt(q))
                        assert lhs == rhs


def check_square_test(max_s=8):
    for s in range(1, max_s + 1):
        for y in words(s + 1):
            lhs = all(
                B(z + (1, 0), y) == B(z + (0, 1), y)
                for z in words(s - 1)
            )
            rhs = y[-2] != y[-1]
            assert lhs == rhs


def check_localized_pairs(max_d=9):
    for d in range(1, max_d + 1):
        W = words(d)
        actual = set()
        for u in W:
            for v in W:
                if wt(u) != wt(v) + 1:
                    continue
                k = wt(v)
                if all(
                    wt(z) in (k, k + 1) or (B(u, z) ^ B(v, z)) == 0
                    for z in W
                ):
                    actual.add((u, v))

        expected = {(t + (1,), t + (0,)) for t in words(d - 1)}
        if d >= 3 and d % 2 == 1:
            k = (d - 1) // 2
            u = (1,) + tuple(a for _ in range(k) for a in (1, 0))
            v = (0,) + tuple(a for _ in range(k) for a in (0, 1))
            expected.add((u, v))
            for z in W:
                assert (B(u, z) ^ B(v, z)) == int(wt(z) in (k, k + 1))
        assert actual == expected


def check_cancellation_and_cross_rigidity(max_n=8):
    for n in range(max_n + 1):
        prefixes = dyck_prefixes(n)
        for P in prefixes:
            block_map = blocks(P)
            _, unmatched = matching(P)
            all_words = [x for A in block_map.values() for x in A]
            for x in all_words:
                for y in all_words:
                    xbar = tuple(x[i] for i in unmatched)
                    ybar = tuple(y[i] for i in unmatched)
                    assert B(x, y) == B(xbar, ybar)

        for P in prefixes:
            BP = blocks(P)
            for Q in prefixes:
                BQ = blocks(Q)
                cross_constant = True
                for A in BP.values():
                    for C in BQ.values():
                        if len({B(x, y) for x in A for y in C}) > 1:
                            cross_constant = False
                            break
                    if not cross_constant:
                        break
                if cross_constant:
                    assert P == Q


def check_quadratic_equality(max_m=4):
    for m in range(max_m + 1):
        W = words(m)
        parity = m % 2
        candidates = []
        for level in range(m + 1):
            L = [x for x in W if wt(x) == level]
            for mask in range(1, 1 << len(L)):
                A = frozenset(L[i] for i in range(len(L)) if mask >> i & 1)
                if all(B(x, y) == parity for x in A for y in A):
                    candidates.append(A)

        compat = [[False] * len(candidates) for _ in candidates]
        for i in range(len(candidates)):
            for j in range(i + 1, len(candidates)):
                A, C = candidates[i], candidates[j]
                if A.isdisjoint(C) and len({B(x, y) for x in A for y in C}) == 1:
                    compat[i][j] = compat[j][i] = True

        target = 2**m
        actual = set()

        def rec(start, chosen, used, score):
            if score == target:
                actual.add(frozenset(candidates[i] for i in chosen))
                return
            if score > target:
                return
            for i in range(start, len(candidates)):
                A = candidates[i]
                next_score = score + len(A) ** 2
                if next_score > target or not A.isdisjoint(used):
                    continue
                if any(not compat[i][j] for j in chosen):
                    continue
                rec(i + 1, chosen + [i], used | set(A), next_score)

        rec(0, [], set(), 0)
        expected = {
            frozenset(frozenset(A) for A in blocks(P).values())
            for P in dyck_prefixes(m)
        }
        assert actual == expected


def valid_reconstruction(r, pairs):
    W = words(r)
    used = {x for edge in pairs for x in edge}
    C = []
    for u, v in pairs:
        if wt(u) == wt(v) + 1:
            hi, lo = u, v
        elif wt(v) == wt(u) + 1:
            hi, lo = v, u
        else:
            return False
        C.append((hi + (0,), lo + (1,)))
    for z in W:
        if z not in used:
            C.append((z + (0,),))
            C.append((z + (1,),))

    for block in C:
        if len({wt(x) for x in block}) != 1:
            return False
        if any(B(x, y) != (r + 1) % 2 for x in block for y in block):
            return False
    for i in range(len(C)):
        for j in range(i + 1, len(C)):
            if len({B(x, y) for x in C[i] for y in C[j]}) > 1:
                return False
    return True


def partial_matchings(vertices, edges):
    adjacency = {v: [] for v in vertices}
    for a, b in edges:
        adjacency[a].append(b)
        adjacency[b].append(a)

    def rec(remaining):
        if not remaining:
            yield ()
            return
        v = min(remaining)
        rest = set(remaining)
        rest.remove(v)
        for M in rec(frozenset(rest)):
            yield M
        for w in adjacency[v]:
            if w in rest:
                reduced = set(rest)
                reduced.remove(w)
                for M in rec(frozenset(reduced)):
                    yield ((v, w),) + M

    yield from rec(frozenset(vertices))

def check_reconstruction(max_r=4):
    for r in range(max_r + 1):
        W = words(r)
        edges = [
            (a, b)
            for i, a in enumerate(W)
            for b in W[i + 1 :]
            if abs(wt(a) - wt(b)) == 1
        ]
        valid = set()
        seen = set()
        for M in partial_matchings(W, edges):
            key = tuple(sorted(tuple(sorted(e)) for e in M))
            if key in seen:
                continue
            seen.add(key)
            if valid_reconstruction(r, M):
                valid.add(key)

        empty = ()
        if r == 0:
            expected = {empty}
        else:
            canonical = tuple(
                sorted(tuple(sorted((t + (1,), t + (0,)))) for t in words(r - 1))
            )
            expected = {empty, canonical}
        assert valid == expected


def balanced_paths(n):
    return [x for x in words(2 * n) if wt(x) == n]


def family_from_matching(P):
    edges, _ = matching(P)
    return frozenset(
        x for x in balanced_paths(len(P) // 2) if all(x[a] != x[b] for a, b in edges)
    )


def maximal_cliques(adjacency):
    n = len(adjacency)
    all_vertices = (1 << n) - 1

    def bits(mask):
        while mask:
            lsb = mask & -mask
            yield lsb.bit_length() - 1
            mask ^= lsb

    def bronk(R, P, X):
        if P == 0 and X == 0:
            yield R
            return
        union = P | X
        pivot = None
        best = -1
        for u in bits(union):
            score = (P & adjacency[u]).bit_count()
            if score > best:
                best = score
                pivot = u
        candidates = P if pivot is None else P & ~adjacency[pivot]
        for v in list(bits(candidates)):
            yield from bronk(R | (1 << v), P & adjacency[v], X & adjacency[v])
            P &= ~(1 << v)
            X |= 1 << v

    yield from bronk(0, all_vertices, 0)


def check_main_theorem(max_n=4):
    for n in range(1, max_n + 1):
        V = balanced_paths(n)
        adjacency = [0] * len(V)
        for i, j in combinations(range(len(V)), 2):
            if B(V[i], V[j]) == 0:
                adjacency[i] |= 1 << j
                adjacency[j] |= 1 << i

        target = 2**n
        actual = set()
        for mask in maximal_cliques(adjacency):
            size = mask.bit_count()
            assert size <= target
            if size == target:
                actual.add(frozenset(V[i] for i in range(len(V)) if mask >> i & 1))

        expected = {family_from_matching(P) for P in dyck_words(n)}
        assert actual == expected
        print(f"n={n}: {len(actual)} extremal families")


def main():
    check_recurrence()
    print("recurrence through d=8: PASS")
    check_square_test()
    print("square test through s=8: PASS")
    check_localized_pairs()
    print("localized-pair classification through d=9: PASS")
    check_cancellation_and_cross_rigidity()
    print("cancellation and cross-rigidity through length 8: PASS")
    check_quadratic_equality()
    print("quadratic equality classification through m=4: PASS")
    check_reconstruction()
    print("reconstruction through r=4: PASS")
    check_main_theorem()
    print("full extremal classification through n=4: PASS")


if __name__ == "__main__":
    main()