package converters

import (
	"encoding/hex"
)

func hexStringToASCII(hexstr string) (string, error) {
	s, err := hex.DecodeString(hexstr)
	return string(s), err
}
