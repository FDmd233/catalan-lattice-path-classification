# Catalan classification of extremal even-intersecting lattice paths

This repository contains the manuscript **A Catalan Classification of Extremal Even-Intersecting Lattice Paths** by **OpenAI**. It addresses the Catalan classification conjecture for extremal even-intersecting North-East lattice-path families posed by Umesh Shankar.

Shankar proved that a pairwise even-intersecting family of paths from \((0,0)\) to \((n,n)\) has size at most \(2^n\), and constructed one extremal family for each noncrossing perfect matching of \([2n]\). The manuscript proves that every extremal family arises in this way, from a unique noncrossing perfect matching. Consequently, the number of extremal families is the Catalan number \(C_n\).

## Manuscript

- [PDF](paper/paper_en.pdf)
- [LaTeX source](paper/paper_en.tex)

The central structural result classifies the equality cases in the quadratic lemma underlying the upper bound: they are precisely the partitions determined by Dyck prefixes. Cross-rigidity and rigidity of the parity kernel on the Boolean cube then determine the extremal relation.

## Low-dimensional audit

The directory [`audit/`](audit/) contains a separate finite audit of the local identities and classifications used in the proof. It verifies:

- the parity recurrence through dimension 8;
- the localized-pair classification through dimension 9;
- Dyck cancellation and cross-rigidity through length 8;
- the reconstruction dichotomy through dimension 4;
- the complete extremal classification for \(n\le 4\), yielding \(1,2,5,14\) extremal families.

These computations are auxiliary and do not replace the proofs in the manuscript.

```bash
python audit/verify_small_cases.py
```

The expected output is recorded in [`audit/expected_output.txt`](audit/expected_output.txt).

GitHub Actions recompiles the manuscript from `paper/paper_en.tex`, runs the finite audit, and records SHA-256 hashes in [`SHA256SUMS`](SHA256SUMS).

## Source problem

- MathDB #376236: https://mathdb.com/p/376236/catalan-classification-conjecture-for-extremal-even-intersec
- Umesh Shankar, *Oddtown and eventown theorems for lattice paths*, arXiv:2607.23117 (2026), doi:10.48550/arXiv.2607.23117.

## Status

This manuscript is presented as a proposed solution for independent verification and submission to MathDB. No claim of peer-reviewed acceptance is made here.

## AI assistance

OpenAI GPT-5.6 Sol was used during the investigation, proof checking, drafting, and repository preparation.

## Author

OpenAI
