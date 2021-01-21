Noun Compound Senses Dataset
----------------------------

This repository contains the Noun Compound Senses (NCS) dataset, used to assess the representation of idiomaticity in vector space models.

The NCS dataset has data for 280 and 180 noun compounds (NCs) in English and Portuguese, respectively, with different degrees of idiomaticity. For each compound, it contains 3 naturalistic corpus sentences and a neutral context (e.g., _This is a/an NC._).

For all sentences in naturalistic and neutral contexts the dataset includes three variants (P1, P2, and P3) with the following characteristics:

  * P1: The original NC is replaced by a synonym (e.g., _brain_ instead of _gray matter_).
  * P2: The original NC is replaced by its syntactic head and dependent, in two different sentences (e.g., _gray_, and _matter_).
  * P3: Each component of the original NC is replaced by a synonym (e.g., _alligator sobs_ instead of _crocodile tears_).

The NCS dataset contains a total of 5,620 test items for English, and 3,600 for Portuguese, and it is based on the NC Compositionality dataset (Cordeiro _et al._, 2019; Reddy _et al_., 2011).

The Noun Compounds Senses dataset will be presented at EACL 2021:

  * Garcia, Marcos, Tiago Kramer Vieira, Carolina Scarton, Marco Idiart, Aline Villavicencio. 2021. Probing for idiomaticity in vector space models. In _Proceedings of the 16th Conference of the European Chapter of the Association for Computational Linguistics (EACL 2021)_ (forthcoming).

## References
Cordeiro, Silvio, Aline Villavicencio, Marco Idiart, and Carlos Ramisch. 2019. Unsupervised compositionality prediction of nominal compounds. _Computational Linguistics_, 45(1):1–57.

Reddy, Siva, Diana McCarthy, and Suresh Manandhar. 2011. An empirical study on compositionality in compound nouns. In _Fifth International Joint Conference on Natural Language Processing_, IJCNLP 2011, Chiang Mai, Thailand, November 8-13, 2011, pages 210–218. The Association for Computer Linguistics.
