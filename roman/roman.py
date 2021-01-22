from collections import OrderedDict

def int_to_roman(num: int) -> str:
  roman_conv = OrderedDict()
  roman_conv[1000] = "M"
  roman_conv[900] = "CM"
  roman_conv[500] = "D"
  roman_conv[400] = "CD"
  roman_conv[100] = "C"
  roman_conv[90] = "XC"
  roman_conv[50] = "L"
  roman_conv[40] = "XL"
  roman_conv[10] = "X"
  roman_conv[9] = "IX"
  roman_conv[5] = "V"
  roman_conv[4] = "IV"
  roman_conv[1] = "I"

  def roman_num(num: int) -> str:
    for r in roman_conv.keys():
      x, y = divmod(num, r)
      yield roman_conv[r] * x
      num -= (r * x)
      if num <= 0:
        break

  return "".join([a for a in roman_num(num)])
