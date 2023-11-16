package main

func makeGood(s string) string {
	res := []byte{ s[0] }
	for i := 1; i < len(s); i++ {
		if len(res) != 0 && (s[i] == res[len(res) - 1] - 32 || s[i] == res[len(res) - 1] + 32) {
			res = res[:len(res) - 1]
			continue
		}
		res = append(res, s[i])
	}
	return string(res)
}
