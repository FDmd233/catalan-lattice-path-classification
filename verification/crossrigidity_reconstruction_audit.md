# Two all-dimensional rigidity audits: Dyck cross-rigidity and cube reconstruction

This note checks two **non-computational** links between the localized-pair
lemma and the main Catalan classification in `paper/paper_en.tex`.
The notation and $\mathbb F_2$-valued parity kernel $B_m$ agree with
Sections 2--5 of the paper and with Shankar, arXiv:2607.23117,
Lemma 2.3. No finite exhaustive search is used here.

## 1. Cross-rigidity is a genuine induction in every length

For a Dyck prefix $P$, write $\mathcal E(P)$ for its noncrossing
matched edges, $\Omega(P)$ for all binary words opposite on matched
edges and arbitrary on unmatched positions, and
$\mathcal A_\varepsilon(P)$ for the orientation block with
the unmatched bits fixed. Define $P\preccurlyeq Q$ when
$B_m(x,y)=B_m(x',y)$ for every $x,x'$ in the same
$P$-block and every $y\in\Omega(Q)$.

**Claim.**
$
 P\preccurlyeq Q \Longrightarrow
 \mathcal E(P)\subseteq\mathcal E(Q)
 \quad\text{for all lengths }m.
$

*Proof by induction.* Delete the final symbol of both prefixes,
obtaining $P^-,Q^-$. Every word of $\Omega(Q^-)$ extends
to $\Omega(Q)$. Every two words in the same block of $P^-$
extend using the same final bit to a pair in a single block of
$P$: if the last symbol is $D$, the opener is unmatched
in $P^-$ and therefore its bit is fixed within that block.
Because the two prefixes have equal weight, the last-coordinate
correction in
$
 B_m(p\alpha,q\beta)=B_{m-1}(p,q)
 +[\alpha=\beta][\operatorname{wt}p=\operatorname{wt}q]
$
is equal for the two lifted comparisons. Therefore
$P^-\preccurlyeq Q^-$ and, by induction,
$\mathcal E(P^-)\subseteq\mathcal E(Q^-)$.

If $P$ ends in $U$, there are no new edges. Otherwise,
remove the endpoints of every edge of $\mathcal E(P^-)$
*simultaneously* from both prefixes. By the inclusion
already proved, the removed pairs are also matched edges of
$Q^-$. The cancellation lemma says removal preserves
$B_m$ on every pair of words satisfying these matching
constraints. It also preserves the fact that words differ
only by orientations inside fixed $P$-blocks.
Thus the relation $\preccurlyeq$ descends after deletion.

The shortened $P$ is $U^sD$ for $s\ge1$:
every surviving opener before the last $D$ was unmatched.
Its nontrivial blocks consist exactly of
$\{z10,z01\}$ with $z\in\{0,1\}^{s-1}$.
Write $y=y'\beta\gamma$ and let
$h=\operatorname{wt}(z)$, $q=\operatorname{wt}(y')$.
A direct two-step recurrence gives
$
 B_{s+1}(z10,y)+B_{s+1}(z01,y)
 =[h=q]+[\gamma=0][h=q+\beta-1]
                 +[\gamma=1][h=q+\beta].
$
If $\beta\ne\gamma$, this is identically zero.
If $\beta=\gamma$, choose $h=q$, which is
possible since $0\le q\le s-1$; the expression is 1.
Consequently, $P\preccurlyeq Q$ forces the last two
positions of *every* word in $\Omega(Q')$ to have
opposite bits.

Two positions are opposite in every word of a
Dyck-prefix block union if and only if they form a
matching edge: for positions in different edges or
unmatched positions, the orientations/free bits can
be chosen independently to make them equal.
Hence the surviving adjacent edge $\{s,s+1\}$
belongs to $\mathcal E(Q')$. Restoring
the deleted common edges proves that the final
edge of $P$ belongs to $\mathcal E(Q)$.
The claim follows.

If the kernel is constant on each $P$-block times
each $Q$-block, it gives $P\preccurlyeq Q$ and
$Q\preccurlyeq P$. Therefore
$\mathcal E(P)=\mathcal E(Q)$; the matching fixes
all $D$-positions and hence the entire Dyck prefix:
$
 \boxed{P=Q}.
$

## 2. Independent reconstruction of the two singleton partitions

Let the blocks of a weight-homogeneous, parity-compatible
family $\mathcal C$ in dimension $r+1$ have two
split collections equal to the singleton partitions
of $\{0,1\}^r$.

Every nonempty half $C_i^0,C_i^1$ is a singleton.
If $C_i$ is split, two words $z0,z1$
cannot both be in the same block because
$B_{r+1}(z0,z1)=r\bmod2$, whereas internal block
parity must be $r+1\bmod2$.
Nor can $z0$ and $z1$ occur in different blocks
when either one is split, since the opposite half
of the latter would produce an overlap in
$\mathcal G_0$ or $\mathcal G_1$.
Thus each label is either represented by the two
singleton blocks $z0,z1$, or it participates in
exactly one two-element block
$
 \{u0,v1\},\qquad \operatorname{wt}u
 =\operatorname{wt}v+1.
$
Different split blocks use disjoint labels.

Fix such a block and put $k=\operatorname{wt}v$.
For a singleton label $z$, comparison with
both singleton blocks gives simultaneously
$
 \Delta_{u,v}(z)=[\operatorname{wt}z=k+1]
               =[\operatorname{wt}z=k].
$
Therefore $\operatorname{wt}z\notin\{k,k+1\}$
and the difference kernel vanishes there.
For a second split block $\{a0,b1\}$, comparing
the two rows of the $2\times2$ parity matrix gives
$
 \Delta_{u,v}(a)=[\operatorname{wt}a=k+1],
 \qquad
 \Delta_{u,v}(b)=[\operatorname{wt}b=k].
$
(The two labels $u,v$ themselves lie in the
allowed levels.) Hence $\Delta_{u,v}$ is supported
only on weights $k,k+1$.

The separate all-dimensional localized-pair lemma
then classifies every split block as either:

1. a canonical pair $\{t10,t01\}$;
2. in $r=2s+1\ge3$, the single exceptional
   pair $\{1(10)^s0,0(01)^s1\}$.

**Exception is impossible.** The exception has
$\Delta_{u,v}=1$ on both allowed levels.
Every word of weight $s+1$ must therefore
be a high endpoint, and every word of weight $s$
a low endpoint, with no singleton labels.
All other split blocks must be canonical:
their high endpoints end in 1 and their
low endpoints end in 0. If $s\ge2$,
more than one word of weight $s$ ends in 1,
but only the exceptional low endpoint can
have this property; contradiction. For $s=1$,
the exceptional block
$\{1100,0011\}$ and the forced canonical block
$\{0110,0101\}$ have cross-parity matrix
$
 \begin{pmatrix}1&0\\1&0\end{pmatrix},
$
violating cross-constancy.

**All-or-nothing canonical propagation.**
Suppose one canonical pair $\{t10,t01\}$
occurs, $h=\operatorname{wt}t$.
Its difference kernel is
$
 \Delta_{t1,t0}(z)
 =[\operatorname{wt}(z_1\cdots z_{r-1})=h].
$
No label of weight $h$ or $h+1$
can be unpaired. The preceding row/column
equalities force, for each $s\in\{0,1\}^{r-1}$:
$
 \begin{array}{c|c}
  \text{label} & \text{forced role}\\ \hline
  s0,\ \operatorname{wt}s=h & \text{low endpoint}\\
  s1,\ \operatorname{wt}s=h-1 & \text{high endpoint}\\
  s1,\ \operatorname{wt}s=h & \text{high endpoint}\\
  s0,\ \operatorname{wt}s=h+1 & \text{low endpoint}
 \end{array}
$
Each of these roles forces a canonical pair with
prefix weight $h-1,h$, or $h+1$, where feasible.
Iteration along the connected chain of weights
$0,1,\dots,r-1$ forces **all** canonical pairs.

Consequently the only possibilities are:
$
 \mathcal C=
  \bigl\{\{z0\},\{z1\}:z\in\{0,1\}^r\bigr\}
\quad\text{or}\quad
 \mathcal C=
  \bigl\{\{t10,t01\}:t\in\{0,1\}^{r-1}\bigr\}.
$
The latter needs $r\ge1$.
For $r=0$, the former is the only possibility.
This is exactly the reconstruction dichotomy.

## 3. Dependency map and audit boundary

Shankar's original quadratic lemma gives
$\sum_i |A_i|^2\le2^m$. Its equality induction
uses:

- equalities in both split inequalities and
  the elementary $(a+b)^2\le2(a^2+b^2)$;
- cross-rigidity proved in Section 1 above;
- the singleton reconstruction proved in Section 2;
- the localized-pair lemma, separately treated in
  [localized_pair_induction.md](localized_pair_induction.md).

The cube rigidity and final relation-to-matching
reduction still have to be read in conjunction
with Sections 4--5 of `paper/paper_en.tex`.
The two arguments above are independent of
all finite brute-force certificates and of
unpublished external source claims.

As with the original manuscript, these
checks are not an assertion of journal
referee acceptance or a statement that
MathDB has marked the question solved.
