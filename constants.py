
ENERC_KCAL = 5
FAT = 6
CHOCDF = 7
PROCNT = 8
SUGAR = 9
LACS = 10
CAFFN = 11

def get_nutrient_idx():
  nidx = {}

  nidx['ENERC_KCAL'] = ENERC_KCAL
  nidx['CAFFN'] = CAFFN
  nidx['CHOCDF'] = CHOCDF
  nidx['FAT'] = FAT
  nidx['PROCNT'] = PROCNT
  nidx['SUGAR'] = SUGAR
  nidx['LACS'] = LACS
  
  return nidx