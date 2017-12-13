'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.
'''
def main():
	str1  = raw_input()
	str2 = raw_input()
	charDict = {}
	if len(str1) != len(str2):
		return False
	for i in range(len(str1)):
		if charDict.get(str1[i]) is not None:
			if str2[i] != charDict[str1[i]]:
				return False
		else:
			charDict[str1[i]] = str2[i]
	return True


if __name__ == '__main__':
	print main()