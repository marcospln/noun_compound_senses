Noun Compound Senses Dataset
----------------------------

This repository contains the Noun Compound Senses (NCS) dataset, used to assess the representation of idiomaticity in vector space models.

The NCS dataset has data for 280 and 180 noun compounds (NCs) in English and Portuguese, respectively, with different degrees of idiomaticity. For each compound, it contains 3 naturalistic corpus sentences and a neutral context (e.g., _This is a/an NC._).

Due to copyright restrictions we do not release all the original (naturalistic) sentences. Instead, we include a script to obtain them from the ukWaC (Baroni _et al._, 2009) and brWaC (Wagner Filho _et al._, 2018) corpora (see below).

For all sentences in naturalistic and neutral contexts the dataset includes three variants (P1, P2, and P3) with the following characteristics:

  * P1: The original NC is replaced by a synonym (e.g., _brain_ instead of _gray matter_).
  * P2: The original NC is replaced by its syntactic head and dependent, in two different sentences (e.g., _gray_, and _matter_).
  * P3: Each component of the original NC is replaced by a synonym (e.g., _alligator sobs_ instead of _crocodile tears_).

The NCS dataset contains a total of 5,620 test items for English, and 3,600 for Portuguese, and it is based on the NC Compositionality dataset (Cordeiro _et al._, 2019; Reddy _et al_., 2011).

If you use the Noun Compounds Senses dataset, please cite the following paper:

  * Garcia, Marcos, Tiago Kramer Vieira, Carolina Scarton, Marco Idiart and Aline Villavicencio. 2021. Probing for idiomaticity in vector space models. In _Proceedings of the 16th Conference of the European Chapter of the Association for Computational Linguistics (EACL 2021)_. Association for Computational Linguistics.

## Obtaining the sentences

### Requirements
 * Python 3
 * Pandas
 * [ukWaC](https://wacky.sslmit.unibo.it/doku.php?id=download) corpus in XML format (tagged). The 25 files (UKWAC-1.xml to UKWAC-25.xml) should be concatenated into a single one (e.g., `cat UKWAC*xml > UKWAC_full.xml`).
 * [brWaC](https://www.inf.ufrgs.br/pln/wiki/index.php?title=BrWaC) corpus in .conll format (single file `brwac.conll`)

### Building the corpus
Use the script `get_sentences.py` to obtain the sentences from the WaC corpora:

`python3 get_sentences.py --lang en --corpus UKWAC_full.xml`

`python3 get_sentences.py --lang pt --corpus brwac.conll`

This should create the `original_sents.csv` files inside `dataset/lang/naturalistic/`.

## References
Baroni, Marco, Silvia Bernardini, Adriano Ferraresi and Eros Zanchetta. 2009. The WaCky wide web: a collection of very large linguistically processed web-crawled corpora. _Language resources and evaluation_, 43(3), 209-226.

Cordeiro, Silvio, Aline Villavicencio, Marco Idiart and Carlos Ramisch. 2019. Unsupervised compositionality prediction of nominal compounds. _Computational Linguistics_, 45(1):1–57.

Reddy, Siva, Diana McCarthy and Suresh Manandhar. 2011. An empirical study on compositionality in compound nouns. In _Fifth International Joint Conference on Natural Language Processing_, IJCNLP 2011, Chiang Mai, Thailand, November 8-13, 2011, pages 210–218. The Association for Computer Linguistics.

Wagner Filho, Jorge Alberto, Rodrigo Wilkens, Marco Idiart and Aline Villavicencio. 2019. The brWaC Corpus: A New Open Resource for Brazilian Portuguese. In _Proceedings of the Eleventh International Conference on Language Resources and Evaluation (LREC 2018)_. ELRA.
