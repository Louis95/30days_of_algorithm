
def computeParent(left, right, string, n, result):
    if left > n or right > n:
        return 
    if len(string) == 2 * n:
        result.append(string)
        return 
    	# If (left_parent < right_parent):
		# Return 
 
    if (left < n):
        computeParent(left+1, right, string+"(", n, result)
    if (right < left):
        computeParent(left, right+1, string+")", n, result)
    


def ValidParen(n):
    result = []
    computeParent(0, 0, "", n, result)
    return result


print(ValidParen(1000))