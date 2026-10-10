# Independent audit of the final Catalan classification reduction

This supplement verifies the **remaining unbounded steps** after
the localized-pair, cross-rigidity and reconstruction lemmas.
It should be read together with:

- [Localized pairs](localized_pair_induction.md)
- [Cross-rigidity and reconstruction](crossrigidity_reconstruction_audit.md)
- [The complete manuscript](../paper/paper_en.tex)
- Shankar's original [Lemma 2.2 and Lemma 2.3](https://arxiv.org/html/2607.23117).

No finite enumeration is used in this note. The combined dependency
chain covers all integers $n\ge1$; it is not an independently
machine-formalized proof or a statement of MathDB acceptance.

## A. Induction through the equality case of Shankar's inequality

Let $\mathcal C=\{A_i\}$ be a family of disjoint
weight-homogeneous blocks of $\{0,1\}^m$, internally
constant with $B_m=m\bmod2$ and pairwise constant
between different blocks. Split by the last bit:
$$
 A_i^a=\{z:za\in A_i\},\quad a\in\{0,1\};
 \qquad I=\{i:A_i^0,A_i^1\ne\varnothing\}.
$$
Both split families
$$
 \mathcal G_0=\{A_i^0\ne\varnothing\}
               \cup\{A_i^1:i\in I\},
 \qquad
 \mathcal G_1=\{A_i^1\ne\varnothing\}
               \cup\{A_i^0:i\in I\}
$$
have mutually disjoint blocks.
The nontrivial overlap case would give
$z0\in A_j$ and $z1,x0\in A_i$.
Weight-homogeneity forces
$\operatorname{wt}x=\operatorname{wt}z+1$, so
$$
 B_m(z0,x0)=B_m(z1,x0)=m\bmod2,
 \qquad B_m(z0,z1)=m-1\bmod2,
$$
contradicting cross-constancy between $A_i,A_j$.
The remaining hypotheses descend by the one-bit
kernel recurrence.

Shankar's lower-dimensional inequality applied to
$\mathcal G_0,\mathcal G_1$ yields
$$
 \sum_i |A_i|^2\le2^m.
$$
Equality forces equality in **both**
lower-dimensional bounds, and, for each split
block $i\in I$, equality in
$(a_i+b_i)^2\le2(a_i^2+b_i^2)$.
Thus $a_i=b_i$.

By induction the two split families are block
partitions of Dyck prefixes $P,Q$ of length $m-1$.
The original cross-constancy and the fact that
the last-bit correction depends only on weights
imply that $B_{m-1}$ is constant on each
$P$-block times each $Q$-block.
Cross-rigidity then forces $P=Q$.

Delete the common matched-edge coordinates.
The cancellation lemma preserves *all*
kernel equalities, and each block of $P$
collapses to exactly one singleton label.
The residual situation is precisely the
all-dimensional singleton reconstruction
dichotomy proved in the neighboring note.
Its two cases append $U$ or $D$ to $P$,
respectively. This closes the equality
classification induction without skipping
the $m=0$ or unmatched-coordinate cases.
Dyck cancellation directly supplies the converse
equality cases, each with
$2^r(2^k)^2=2^{2k+r}=2^m$.

Uniqueness follows because a pair of positions
has opposite bits in **every** word of
$\Omega(P)$ exactly when those positions are a
matching edge of $P$.

## B. The cube-rigidity induction

Let $\phi:\{0,1\}^r\to\{0,1\}^r$ be a
weight-preserving bijection satisfying
$$
 B_r(\phi(x),\phi(y))=B_r(x,y).
$$
Define a relation on adjacent-weight words
$u,v$ by the support of
$\Delta_{u,v}$ being contained in their two
Hamming-weight levels. The localized-pair
classification shows its graph consists of:

- the disjoint canonical edges $t1\sim t0$,
  one for every $t\in\{0,1\}^{r-1}$;
- for odd $r\ge3$, exactly one further
  edge joining the alternating exceptional pair.

In odd $r$, the endpoints of the exceptional
edge are **the only vertices of graph degree two**;
its edge is therefore fixed setwise by
every automorphism. Remove it to recover the
canonical matching. In even $r$, this matching
was already the whole relation graph.
Weight preservation prevents the two endpoints
of any canonical edge from being swapped, so
$$
 \phi(t\alpha)=\psi(t)\alpha,
$$
for a weight-preserving bijection
$\psi:\{0,1\}^{r-1}\to\{0,1\}^{r-1}$.
The identity
$$
 B_r(t0,s1)=B_{r-1}(t,s)
$$
holds for **all** $t,s$ (last bits differ),
and forces $\psi$ to preserve the same kernel.
Starting with $r=0,1$, induction gives
$\psi=\mathrm{id}$ and hence
$$
 \boxed{\phi=\mathrm{id}}.
$$

## C. Exactness of the extremal-relation argument

For a balanced path $F$ of length $2n$, define
$$
 u(F)=(f_1,\dots,f_n),\quad
 v(F)=(1-f_{2n},\dots,1-f_{n+1}).
$$
This is a bijection between balanced paths and
pairs $(u,v)$ of equal weight. Shankar's
reflection identity gives
$$
 B_{2n}(F,G)=B_n(u(F),u(G))+B_n(v(F),v(G)).
$$
Therefore an even-intersecting extremal family
corresponds to a relation $R$ with
$|R|=2^n$, equal weights in each pair,
and $B_n(u,u')=B_n(v,v')$ for all
pairs of members.

Build the bipartite graph with edges $R$,
omitting isolated vertices. If two vertices on
one side are joined by an alternating path
of length $2j$, the parity compatibility
transfers their kernel value to an alternating
path of length $2j-2$ on the opposite side.
Induction in $j$ gives internal parity
$n\bmod2$. Connectivity also gives
cross-constancy between different components.
Consequently the left and right component
families satisfy Shankar's quadratic lemma.

The chain
$$
 |R|\le\sum_j |A_j||B_j|
 \le\Bigl(\sum_j|A_j|^2\Bigr)^{1/2}
     \Bigl(\sum_j|B_j|^2\Bigr)^{1/2}
 \le2^n
$$
has equality throughout. Thus every graph
component is complete bipartite, and both
component partitions are Dyck-prefix equality
partitions. The number of components forces
their unmatched counts to be equal; hence
both sides have the same number $k$ of
matched edges. Their pairing induces a
weight- and $B_r$-preserving bijection
of unmatched labels. Cube rigidity makes it
the identity:
$$
 R=\bigcup_{\varepsilon\in\{0,1\}^r}
 \mathcal A_\varepsilon(P)
 \times\mathcal A_\varepsilon(Q).
$$

## D. Construction and uniqueness of the noncrossing matching

Take all matched edges of $P$ in the first
half, all reflected matched edges of $Q$
in the second half, and match their $r$
unmatched positions across the middle in
opposite order. Cross-half edges are nested;
no unmatched position lies inside any
internal Dyck matching edge.
The resulting perfect matching $M$ is
noncrossing. Every word from the displayed
relation is opposite on each edge of $M$,
so its path belongs to $\mathcal F_M$.
Both sides have $2^n$ members and
therefore coincide.

Finally, the rule
$$
 \{i,j\}\in M
 \quad\Longleftrightarrow\quad
 w_i\ne w_j\quad\text{for every }w\in\mathcal F_M
$$
reconstructs $M$: if positions $i,j$
are on separate edges, orient those two
edges independently to make their bits equal.
Thus the matching is **unique**.
Since the noncrossing perfect matchings
of $[2n]$ are counted by $C_n$,
the claimed equality classification is
derived for every $n\ge1$.

## Scope of this audit

Sections A--D supply an independent reading
of every **global logical interface** from
Shankar's inequality to the Catalan theorem.
The only local finite-state input is the
all-dimensional lemma separately expanded
in `localized_pair_induction.md`.
Together, the three verification notes
cover the manuscript's entire main proof
architecture without invoking a finite
exhaustion of all paths in arbitrary dimension.

This supports a substantially stronger
mathematical audit outcome than small-case
verification alone, but it is **not**
journal acceptance or machine formalization.
The public MathDB question may still
have status "open" until an independent
review or solution posting is recognized.
No manuscript main theorem or author
attribution is changed by this document.
