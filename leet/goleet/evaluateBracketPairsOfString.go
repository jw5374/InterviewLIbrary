package main

func EvaluateBracketStrings(s string, knowledge [][]string) string {
    var knowledgeMap map[string]string = make(map[string]string)
    var res string = ""
    for _, pair := range knowledge {
        knowledgeMap[pair[0]] = pair[1]
    }
    i := 0
    for i < len(s) {
        switch string(s[i]) {
            case "(":
                j := i+1
                for j < len(s) && string(s[j]) != ")" {
                    j++
                }
                if val, exists := knowledgeMap[string(s[i+1:j])]; !exists {
                    res += "?"
                } else {
                    res += val
                }
                i = j + 1
            default:
                res += string(s[i])
                i++
        }
    }
    return res
}
