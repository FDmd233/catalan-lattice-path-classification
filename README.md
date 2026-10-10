# A Catalan Classification of Extremal Even-Intersecting Lattice Paths

This repository contains the manuscript **A Catalan Classification of Extremal Even-Intersecting Lattice Paths** by **OpenAI**. It addresses the Catalan classification conjecture for extremal even-intersecting North--East lattice-path families posed by Umesh Shankar.

Shankar proved that a pairwise even-intersecting family of paths from $(0,0)$ to $(n,n)$ has size at most $2^n$, and constructed one extremal family for each noncrossing perfect matching of $[2n]$. The manuscript proves that every extremal family arises in this way, from a unique noncrossing perfect matching. Consequently, the number of extremal families is the Catalan number $C_n$.

## Manuscript

- [PDF](paper/paper_en.pdf)
- [LaTeX source](paper/paper_en.tex)

The central structural result classifies the equality cases in the quadratic lemma underlying the upper bound: they are exactly the partitions determined by Dyck prefixes. Cross-rigidity and rigidity of the parity kernel on the Boolean cube then determine the extremal relation.

## Finite audit

The directory [`audit/`](audit/) contains a separate finite audit of the local identities and low-dimensional classifications used in the proof. It checks:

- the parity recurrence through dimension 8;
- the localized-pair classification through dimension 9;
- Dyck cancellation and cross-rigidity through length 8;
- the quadratic equality classification through dimension 4;
- the reconstruction dichotomy through dimension 4;
- the complete extremal classification for $n\le 4$, yielding $1,2,5,14$ extremal families.

These computations are auxiliary and do not replace the proofs in the manuscript.

~~~bash
python audit/verify_small_cases.py
~~~

The expected output is recorded in [`audit/expected_output.txt`](audit/expected_output.txt). GitHub Actions recompiles the manuscript, runs the finite audit, and records SHA-256 hashes in [`SHA256SUMS`](SHA256SUMS).

## All-dimensional proof audit

The [localized-pair induction audit](verification/localized_pair_induction.md) expands every final-bit transition of the central finite-state classification, including the odd-dimensional alternating exception and all endpoint cases. Unlike the finite audit, this is an **all-dimensional symbolic induction**. It covers one key lemma only; the full Catalan theorem still depends on the manuscript's separate cross-rigidity, reconstruction, and extremal-relation proofs.

- [All-dimensional cross-rigidity and reconstruction proofs](verification/crossrigidity_reconstruction_audit.md) independently check both the inclusion of Dyck-prefix matching edges and the all-or-nothing reconstruction of canonical split blocks. The arguments use no finite search and make their remaining dependencies explicit.

- [Complete final-reduction audit](verification/final_classification_proof_audit.md) independently traces Shankar's quadratic equality, cube rigidity, extremal bipartite relations, and the unique noncrossing matching for arbitrary \(n\). Together with the two preceding supplements, this covers the **whole mathematical dependency chain**, without claiming machine formalization or MathDB acceptance.

## Source problem

- [MathDB #376236](https://mathdb.com/p/376236/catalan-classification-conjecture-for-extremal-even-intersec)
- Umesh Shankar, *Oddtown and eventown theorems for lattice paths*, arXiv:2607.23117 (2026), [DOI](https://doi.org/10.48550/arXiv.2607.23117)

## Status

This manuscript is presented as a proposed solution for independent verification and submission to MathDB. No claim of peer-reviewed acceptance is made here.

## AI assistance

OpenAI GPT-5.6 Sol was used during the investigation, proof checking, drafting, and repository preparation.

## Author

OpenAI
