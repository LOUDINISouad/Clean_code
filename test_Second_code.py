def get_symbol(name: str) -> str:
  chemical_symbols = {
      "Hydrogen": "H",
      "Helium": "He",
      "Lithium": "Li",
      
  }

  symbol = chemical_symbols.get(name)
  if symbol:
    return symbol
  else:
    print(f"Symbol for element '{name}' not found")
    return "not found"

# Test cases
print(get_symbol(name="Hydrogen"))  # Output: H
print(get_symbol(name="Iron"))       # Output: Symbol for element 'Iron' not found

def test ():
  assert get_symbol(name="Hydrogen") == "H"            
  assert get_symbol(name="Helium") == "He"
  

