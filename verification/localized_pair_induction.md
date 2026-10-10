# Independent transition audit for the localized-pair lemma

This proof supplement expands the finite-state induction used in Lemma
\`localized pairs\` of \`paper/paper_en.tex\`. It is an **all-dimensions
symbolic argument**, not a bounded computation. It establishes only
the local classification lemma and its boundary cases; the global
Catalan conclusion additionally relies on the cross-rigidity and
reconstruction steps of the manuscript.

## Kernel recurrence

For words $x,y,z\in\{0,1\}^d$, write
$$
\Delta_{x,y}^{(d)}(z)=B_d(x,z)+B_d(y,z).
$$
Write $\mathcal L_j^{(d)}=\{z:\operatorname{wt}(z)=j\}$, with an
out-of-range layer interpreted as empty.
For $x=p\alpha,\ y=q\beta$, and a test word $z\gamma$,
$$
\Delta_{p\alpha,q\beta}^{(d)}(z\gamma)
=\Delta_{p,q}^{(d-1)}(z)
 +[\alpha=\gamma][\operatorname{wt}p=\operatorname{wt}z]
 +[\beta=\gamma][\operatorname{wt}q=\operatorname{wt}z].
\tag{*}
$$
All operations in (*) are in $\mathbb F_2$. A terminal pattern
is *feasible* only if the prescribed prefix weights belong to
$0,\ldots,d-1$.

## Six states

Use these state names, with all weights evaluated in length $d$:

| State | Weights $(x,y)$ | Required profile |
|---|---|---|
| $S_d(k)$ | $(k,k)$ | support only in $\mathcal L_k$ |
| $E_d(k)$ | $(k,k)$ | exactly $\mathbf1_{\mathcal L_k}$ |
| $L^-_d(k)$ | $(k+1,k)$ | support only in $\mathcal L_k$ |
| $L^+_d(k)$ | $(k+1,k)$ | support only in $\mathcal L_{k+1}$ |
| $M_d(k)$ | $(k+1,k-1)$ | support only in $\mathcal L_k$ |
| $T_d(k)$ | $(k+1,k)$ | exactly $\mathbf1_{\mathcal L_k\cup\mathcal L_{k+1}}$ |

An $S_d(k)$ state must have $x=y$.
The states $E_d(k),L^-_d(k),L^+_d(k)$ do not exist.
The two exceptional states $M,T$ do exist, but are uniquely
determined and alternate in the word length.

## Closed transition table for the impossible states

The following are consequences of (*) at the indicated Hamming-weight
layers; $(\alpha,\beta)$ is the pair of final bits:

| State | 00 | 01 | 10 | 11 |
|---|---|---|---|---|
| $S_d(k)$ | prefix $S_{d-1}(k)$ | prefix $L^+_{d-1}(k-1)$ | prefix $L^-_{d-1}(k-1)$, after exchanging $p,q$ | prefix $S_{d-1}(k-1)$ |
| $E_d(k)$ | impossible | adjacent-weight prefix with zero profile | adjacent-weight prefix with zero profile | impossible |
| $L^-_d(k)$ | impossible | impossible | prefix $E_{d-1}(k)$ | prefix $L^+_{d-1}(k-1)$ |

For example, in $L^-_d(k)$, terminal pattern 00 forces
$\Delta_{p,q}^{(d-1)}(z)=1$ at $\mathrm{wt}(z)=k+1$
by testing $z0$, and forces the same value to be 0 by
testing $z1$; this level is feasible because $x$
ends in 0 and has weight $k+1$.
The same argument rules out pattern 01.
Pattern 10 forces the exact profile
$\mathbf1_{\mathcal L_k}$ of an $E$-state, and
pattern 11 forces a profile supported in the upper of
two adjacent layers, an $L^+$-state.
Complementing $x,y,z$ simultaneously and exchanging $x,y$
sends $L^+_d(k)$ to $L^-_d(d-k-1)$.
For the $E$-state, terminal patterns 00 and 11 force
different target values for $z0,z1$ when the prefix
has weight $k$, respectively $k-1$; the
corresponding layer is feasible. Unequal terminal bits
force a zero profile for adjacent prefix weights, a
special case of both $L^-$ and $L^+$ and hence impossible.

The row for $S$, combined with these impossibilities,
forces equal last bits and then identical prefixes by induction.
Starting at $d=0$ proves the three impossibility assertions and
$S_d(k)\Rightarrow x=y$ simultaneously.

## Alternating states and exact boundary cases

The remaining transition table is:

| State | 00 | 01 | 10 | 11 |
|---|---|---|---|---|
| $M_d(k)$ | impossible | impossible | $T_{d-1}(k-1)$ | impossible |
| $T_d(k)$, $d>1$ | impossible | $M_{d-1}(k)$ | impossible | impossible |

The contradictions in $M_d(k)$ arise at the feasible
prefix-weight levels $k+1$ for 00/01 and $k-2$
for 11. The $T$-state rules out 00/11 by comparing
$z0,z1$ at a feasible prefix word of weight $k$.
For its 10 pattern, use a test word of prefix weight
$k-1$ if $k>0$; if $k=0$, use prefix weight 1,
which exists because $d>1$. Both choices force different
profiles for $z0,z1$ even though (*) would make
them equal.

The **only** base state is $T_1(0)=(1,0)$;
no $M_1$ state is feasible. Iterating the unique allowed
transitions gives precisely
$$
M_{2k}(k):
 \bigl(11(01)^{k-1},00(10)^{k-1}\bigr)
 \quad(k\ge1),
$$
and
$$
T_{2k+1}(k):
 \bigl(1(10)^k,0(01)^k\bigr)
 \quad(k\ge0).
$$
Other parameter or parity choices are impossible.

## Localized pairs: final case split

Assume $\operatorname{wt}(u)=k+1$,
$\operatorname{wt}(v)=k$, and
$\Delta_{u,v}$ is supported in
$\mathcal L_k\cup\mathcal L_{k+1}$.
The four final-bit patterns imply:

| Last bits of $u,v$ | Prefix state | Consequence |
|---|---|---|
| 00 | $L^-_{d-1}(k)$ | impossible |
| 11 | $L^+_{d-1}(k-1)$ | impossible |
| 10 | $S_{d-1}(k)$ | $u=t1,\ v=t0$ |
| 01 | $M_{d-1}(k)$ | $d=2k+1\ge3,\ u=1(10)^k,\ v=0(01)^k$ |

At $d=1$ the nominal alternating state coincides
with the canonical pair, so is not a new exception.
This proves the localized-pair statement **for all**
$d\ge1$.

## Independent review boundary

The above formal transition check fills in the
abbreviated induction in the source and is not based
on finite-word testing. Cross-rigidity, reconstruction,
and the reduction to extremal lattice-path relations
are separate theorems and require their own review.
No author attribution or manuscript theorem is changed.
