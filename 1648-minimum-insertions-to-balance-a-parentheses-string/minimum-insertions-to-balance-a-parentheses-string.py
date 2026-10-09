class Solution:
  def minInsertions(self, s: str) -> int:
    res = 0  # Total insertions needed
    open_brackets = 0  # Count of unmatched '('
    i = 0
    n = len(s)

    while i < n:
      if s[i] == '(':
        open_brackets += 1
        i += 1
      else:
        # We see a closing parenthesis ')'
        # Check if the next character is also ')'
        if i + 1 < n and s[i + 1] == ')':
          i += 2  # Consumed a pair ')'
        else:
          res += 1  # Need to insert one ')' to make a pair ')'
          i += 1  # Consumed single ')'

        if open_brackets > 0:
          open_brackets -= 1
        else:
          res += 1  # Need to insert an opening '(' for this pair

    # Each remaining unmatched '(' needs two ')'
    res += open_brackets * 2
    return res
