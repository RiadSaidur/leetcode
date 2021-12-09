class Solution(object):
  def subtractProductAndSum(self, n):
    """
    :type n: int
    :rtype: int
    """
    import numpy

    digits = list(int(digit) for digit in str(n))

    return numpy.prod(digits) - sum(digits)
    