# References

Papers and repositories behind the PAN-2012 data decisions. This directory holds citations and notes
only: no PDFs, no data. Add a paper here by giving its full citation, where to obtain it, and what we
used it for, so each decision can be traced to a source.

## Datasets and competitions

### Inches and Crestani (2012)

- **Citation:** Giacomo Inches and Fabio Crestani. 2012. Overview of the International Sexual Predator
  Identification Competition at PAN-2012. In *CLEF 2012 Evaluation Labs and Workshop, Online Working
  Notes*, vol. 30.
- **Data:** PAN-2012 on Zenodo, DOI 10.5281/zenodo.3713280 (provenance and checksums in `data/README.md`).
- **Used for:** how the corpus was built (Perverted-Justice positives, Omegle and IRC negatives, 25-minute
  segmentation, 150-message cap); problem 1 (predator authors) as the label and problem 2 (suspicious
  lines) as a participant-submitted, single-expert label that cannot define positives (sections 2.1, 4.2).

### Villatoro-Tello et al. (2012)

- **Citation:** Esaú Villatoro-Tello, Antonio Juárez-González, Hugo Jair Escalante, Manuel Montes-y-Gómez,
  and Luis Villaseñor-Pineda. 2012. A Two-step Approach for Effective Detection of Misbehaving Users in
  Chats. Notebook for PAN at CLEF 2012, *CLEF Online Working Notes*, vol. 1178.
- **Used for:** origin of VTPAN (the pre-filtering in section 3.2, Tables 1 and 5); an independent use of
  "conversation is suspicious if at least one predator appears in it"; the count cross-check in
  `docs/pan2012-structure.md`.

## Early detection

### Vogt, Leser and Akbik (2021)

- **Citation:** Matthias Vogt, Ulf Leser, and Alan Akbik. 2021. Early Detection of Sexual Predators in
  Chats. In *Proceedings of the 59th Annual Meeting of the ACL and the 11th IJCNLP (Volume 1: Long
  Papers)*, pp. 4985-4999.
- **Code:** `https://gitlab.com/early-sexual-predator-detection/eSPD-datasets` (MIT-licensed processing
  code; PAN-2012 and ChatCoder2 data are not included).
- **Used for:** defining early detection and latency-weighted F1 (section 3.2); why PAN-2012 segments are
  a weak basis for earliness; PANC construction; that some segments over 150 messages were not filtered;
  VTPAN described in section 2.2.2.

### An et al. (2025)

- **Citation:** Jinmyeong An, Sangwon Ryu, Heejin Do, Yunsu Kim, Jungseul Ok, and Gary Geunbae Lee. 2025.
  Revisiting Early Detection of Sexual Predators via Turn-level Optimization. In *Proceedings of NAACL 2025
  (Volume 1: Long Papers)*, pp. 4713-4724.
- **Code:** `https://github.com/jinmyeongAN/SCoRL` (from the paper's footnote).
- **Used for:** the latency-weighted F1 equations (1)-(3) as applied to turns; the PANC statistics and the
  10:1 downsampled test set; hard negatives (cybersex between adults) as the main false-positive risk.

## Notes on use

- The ChatCoder2 corpus is available from its authors on request only and must not be redistributed;
  PANC needs it, so this project does not assume PANC or VTPAN are available (see
  `docs/pan2012-structure.md`).
- Claims drawn from these papers should cite the section or table, as the findings doc does.
