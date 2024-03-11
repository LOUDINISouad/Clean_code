def get_symbol(name: str) -> str:
   chemical_symbols = {}
   symbol = chemical_symbols.get(name)
   if symbol:
       return symbol

   print("symbol not found")
   return "not found"




