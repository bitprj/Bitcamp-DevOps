import src
from src.fibonacci import recur_fibo

def test_smallFib():
  assert recur_fibo(1) == 1, "Should be 1"
  
def test_biggerFib():
  assert recur_fibo(10) == 55, "Should be 55"
