package converters

import (
	"fmt"
	"testing"
)

func TestHexStringToASCII(t *testing.T) {
	s, err := hexStringToASCII("b9871e23340cb47da2d8c76828cca80f4c641a806dee842104bfd71a0902a5")
	if err == nil {
		fmt.Println(string(s))
	} else {
		fmt.Println(err)
	}
}
