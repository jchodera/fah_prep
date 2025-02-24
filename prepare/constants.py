# REMARK 350 (biological multimer symmetry operations) from 5RGG
# TODO: Remove this when REMARK 350 is restored
BIOLOGICAL_SYMMETRY_HEADER = """\
REMARK 350
REMARK 350 COORDINATES FOR A COMPLETE MULTIMER REPRESENTING THE KNOWN
REMARK 350 BIOLOGICALLY SIGNIFICANT OLIGOMERIZATION STATE OF THE
REMARK 350 MOLECULE CAN BE GENERATED BY APPLYING BIOMT TRANSFORMATIONS
REMARK 350 GIVEN BELOW.  BOTH NON-CRYSTALLOGRAPHIC AND
REMARK 350 CRYSTALLOGRAPHIC OPERATIONS ARE GIVEN.
REMARK 350
REMARK 350 BIOMOLECULE: 1
REMARK 350 AUTHOR DETERMINED BIOLOGICAL UNIT: DIMERIC
REMARK 350 SOFTWARE DETERMINED QUATERNARY STRUCTURE: DIMERIC
REMARK 350 SOFTWARE USED: PISA
REMARK 350 TOTAL BURIED SURFACE AREA: 4170 ANGSTROM**2
REMARK 350 SURFACE AREA OF THE COMPLEX: 25430 ANGSTROM**2
REMARK 350 CHANGE IN SOLVENT FREE ENERGY: -3.0 KCAL/MOL
REMARK 350 APPLY THE FOLLOWING TO CHAINS: A
REMARK 350   BIOMT1   1  1.000000  0.000000  0.000000        0.00000
REMARK 350   BIOMT2   1  0.000000  1.000000  0.000000        0.00000
REMARK 350   BIOMT3   1  0.000000  0.000000  1.000000        0.00000
REMARK 350   BIOMT1   2 -1.000000  0.000000  0.000000        0.00000
REMARK 350   BIOMT2   2  0.000000  1.000000  0.000000        0.00000
REMARK 350   BIOMT3   2  0.000000  0.000000 -1.000000        0.00000
"""

SEQRES_MONOMER = """\
SEQRES   1 A  306  SER GLY PHE ARG LYS MET ALA PHE PRO SER GLY LYS VAL
SEQRES   2 A  306  GLU GLY CYS MET VAL GLN VAL THR CYS GLY THR THR THR
SEQRES   3 A  306  LEU ASN GLY LEU TRP LEU ASP ASP VAL VAL TYR CYS PRO
SEQRES   4 A  306  ARG HIS VAL ILE CYS THR SER GLU ASP MET LEU ASN PRO
SEQRES   5 A  306  ASN TYR GLU ASP LEU LEU ILE ARG LYS SER ASN HIS ASN
SEQRES   6 A  306  PHE LEU VAL GLN ALA GLY ASN VAL GLN LEU ARG VAL ILE
SEQRES   7 A  306  GLY HIS SER MET GLN ASN CYS VAL LEU LYS LEU LYS VAL
SEQRES   8 A  306  ASP THR ALA ASN PRO LYS THR PRO LYS TYR LYS PHE VAL
SEQRES   9 A  306  ARG ILE GLN PRO GLY GLN THR PHE SER VAL LEU ALA CYS
SEQRES  10 A  306  TYR ASN GLY SER PRO SER GLY VAL TYR GLN CYS ALA MET
SEQRES  11 A  306  ARG PRO ASN PHE THR ILE LYS GLY SER PHE LEU ASN GLY
SEQRES  12 A  306  SER CYS GLY SER VAL GLY PHE ASN ILE ASP TYR ASP CYS
SEQRES  13 A  306  VAL SER PHE CYS TYR MET HIS HIS MET GLU LEU PRO THR
SEQRES  14 A  306  GLY VAL HIS ALA GLY THR ASP LEU GLU GLY ASN PHE TYR
SEQRES  15 A  306  GLY PRO PHE VAL ASP ARG GLN THR ALA GLN ALA ALA GLY
SEQRES  16 A  306  THR ASP THR THR ILE THR VAL ASN VAL LEU ALA TRP LEU
SEQRES  17 A  306  TYR ALA ALA VAL ILE ASN GLY ASP ARG TRP PHE LEU ASN
SEQRES  18 A  306  ARG PHE THR THR THR LEU ASN ASP PHE ASN LEU VAL ALA
SEQRES  19 A  306  MET LYS TYR ASN TYR GLU PRO LEU THR GLN ASP HIS VAL
SEQRES  20 A  306  ASP ILE LEU GLY PRO LEU SER ALA GLN THR GLY ILE ALA
SEQRES  21 A  306  VAL LEU ASP MET CYS ALA SER LEU LYS GLU LEU LEU GLN
SEQRES  22 A  306  ASN GLY MET ASN GLY ARG THR ILE LEU GLY SER ALA LEU
SEQRES  23 A  306  LEU GLU ASP GLU PHE THR PRO PHE ASP VAL VAL ARG GLN
SEQRES  24 A  306  CYS SER GLY VAL THR PHE GLN
"""

SEQRES_DIMER = """\
SEQRES   1 A  306  SER GLY PHE ARG LYS MET ALA PHE PRO SER GLY LYS VAL
SEQRES   2 A  306  GLU GLY CYS MET VAL GLN VAL THR CYS GLY THR THR THR
SEQRES   3 A  306  LEU ASN GLY LEU TRP LEU ASP ASP VAL VAL TYR CYS PRO
SEQRES   4 A  306  ARG HIS VAL ILE CYS THR SER GLU ASP MET LEU ASN PRO
SEQRES   5 A  306  ASN TYR GLU ASP LEU LEU ILE ARG LYS SER ASN HIS ASN
SEQRES   6 A  306  PHE LEU VAL GLN ALA GLY ASN VAL GLN LEU ARG VAL ILE
SEQRES   7 A  306  GLY HIS SER MET GLN ASN CYS VAL LEU LYS LEU LYS VAL
SEQRES   8 A  306  ASP THR ALA ASN PRO LYS THR PRO LYS TYR LYS PHE VAL
SEQRES   9 A  306  ARG ILE GLN PRO GLY GLN THR PHE SER VAL LEU ALA CYS
SEQRES  10 A  306  TYR ASN GLY SER PRO SER GLY VAL TYR GLN CYS ALA MET
SEQRES  11 A  306  ARG PRO ASN PHE THR ILE LYS GLY SER PHE LEU ASN GLY
SEQRES  12 A  306  SER CYS GLY SER VAL GLY PHE ASN ILE ASP TYR ASP CYS
SEQRES  13 A  306  VAL SER PHE CYS TYR MET HIS HIS MET GLU LEU PRO THR
SEQRES  14 A  306  GLY VAL HIS ALA GLY THR ASP LEU GLU GLY ASN PHE TYR
SEQRES  15 A  306  GLY PRO PHE VAL ASP ARG GLN THR ALA GLN ALA ALA GLY
SEQRES  16 A  306  THR ASP THR THR ILE THR VAL ASN VAL LEU ALA TRP LEU
SEQRES  17 A  306  TYR ALA ALA VAL ILE ASN GLY ASP ARG TRP PHE LEU ASN
SEQRES  18 A  306  ARG PHE THR THR THR LEU ASN ASP PHE ASN LEU VAL ALA
SEQRES  19 A  306  MET LYS TYR ASN TYR GLU PRO LEU THR GLN ASP HIS VAL
SEQRES  20 A  306  ASP ILE LEU GLY PRO LEU SER ALA GLN THR GLY ILE ALA
SEQRES  21 A  306  VAL LEU ASP MET CYS ALA SER LEU LYS GLU LEU LEU GLN
SEQRES  22 A  306  ASN GLY MET ASN GLY ARG THR ILE LEU GLY SER ALA LEU
SEQRES  23 A  306  LEU GLU ASP GLU PHE THR PRO PHE ASP VAL VAL ARG GLN
SEQRES  24 A  306  CYS SER GLY VAL THR PHE GLN
SEQRES   1 B  306  SER GLY PHE ARG LYS MET ALA PHE PRO SER GLY LYS VAL
SEQRES   2 B  306  GLU GLY CYS MET VAL GLN VAL THR CYS GLY THR THR THR
SEQRES   3 B  306  LEU ASN GLY LEU TRP LEU ASP ASP VAL VAL TYR CYS PRO
SEQRES   4 B  306  ARG HIS VAL ILE CYS THR SER GLU ASP MET LEU ASN PRO
SEQRES   5 B  306  ASN TYR GLU ASP LEU LEU ILE ARG LYS SER ASN HIS ASN
SEQRES   6 B  306  PHE LEU VAL GLN ALA GLY ASN VAL GLN LEU ARG VAL ILE
SEQRES   7 B  306  GLY HIS SER MET GLN ASN CYS VAL LEU LYS LEU LYS VAL
SEQRES   8 B  306  ASP THR ALA ASN PRO LYS THR PRO LYS TYR LYS PHE VAL
SEQRES   9 B  306  ARG ILE GLN PRO GLY GLN THR PHE SER VAL LEU ALA CYS
SEQRES  10 B  306  TYR ASN GLY SER PRO SER GLY VAL TYR GLN CYS ALA MET
SEQRES  11 B  306  ARG PRO ASN PHE THR ILE LYS GLY SER PHE LEU ASN GLY
SEQRES  12 B  306  SER CYS GLY SER VAL GLY PHE ASN ILE ASP TYR ASP CYS
SEQRES  13 B  306  VAL SER PHE CYS TYR MET HIS HIS MET GLU LEU PRO THR
SEQRES  14 B  306  GLY VAL HIS ALA GLY THR ASP LEU GLU GLY ASN PHE TYR
SEQRES  15 B  306  GLY PRO PHE VAL ASP ARG GLN THR ALA GLN ALA ALA GLY
SEQRES  16 B  306  THR ASP THR THR ILE THR VAL ASN VAL LEU ALA TRP LEU
SEQRES  17 B  306  TYR ALA ALA VAL ILE ASN GLY ASP ARG TRP PHE LEU ASN
SEQRES  18 B  306  ARG PHE THR THR THR LEU ASN ASP PHE ASN LEU VAL ALA
SEQRES  19 B  306  MET LYS TYR ASN TYR GLU PRO LEU THR GLN ASP HIS VAL
SEQRES  20 B  306  ASP ILE LEU GLY PRO LEU SER ALA GLN THR GLY ILE ALA
SEQRES  21 B  306  VAL LEU ASP MET CYS ALA SER LEU LYS GLU LEU LEU GLN
SEQRES  22 B  306  ASN GLY MET ASN GLY ARG THR ILE LEU GLY SER ALA LEU
SEQRES  23 B  306  LEU GLU ASP GLU PHE THR PRO PHE ASP VAL VAL ARG GLN
SEQRES  24 B  306  CYS SER GLY VAL THR PHE GLN
"""

FRAGALYSIS_URL='https://fragalysis.diamond.ac.uk/media/targets/Mpro.zip'

CHAIN_PDB_INDEX = 21

MINIMUM_FRAGMENT_SIZE = 7