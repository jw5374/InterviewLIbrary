package main

import (
	"fmt"
	"strconv"
)

func Tree2str(root *TreeNode) string {
    if root == nil {
        return ""
    }
    if root.Left == nil && root.Right == nil {
        return strconv.Itoa(root.Val)
    }
    if root.Right == nil {
        return fmt.Sprintf("%s(%s)%s", strconv.Itoa(root.Val), Tree2str(root.Left), Tree2str(root.Right))
    }
    return fmt.Sprintf("%s(%s)(%s)", strconv.Itoa(root.Val), Tree2str(root.Left), Tree2str(root.Right))
}
