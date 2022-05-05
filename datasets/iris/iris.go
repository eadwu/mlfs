package main

import "C"
import (
	"mlfs/api"
	"unsafe"

	"google.golang.org/protobuf/proto"
)

// Iris-specific return codes enum
type irisCode int8

const (
	// error_SUCCESS is the equivalent to a 0 exit code
	error_SUCCESS = irisCode(iota)
	// error_FAILED_TO_SERIALIZE_DATA is returned when proto.Marshal fails
	error_FAILED_TO_SERIALIZE_DATA
)

// Links to downloads
type irisMetadata struct {
	link string
	hash string
}

var (
	INDEX   = irisMetadata{"https://archive.ics.uci.edu/ml/machine-learning-databases/iris/Index", ""}
	ORIG    = irisMetadata{"https://archive.ics.uci.edu/ml/machine-learning-databases/iris/bezdekIris.data", ""}
	DATASET = irisMetadata{"https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", ""}
	DESC    = irisMetadata{"https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.names", ""}
)

//export downloadIris
func downloadIris() (unsafe.Pointer, C.ushort) {
	dataset := &api.Dataset{}

	payload, err := proto.Marshal(dataset)
	if err != nil {
		return nil, C.ushort(error_FAILED_TO_SERIALIZE_DATA)
	}

	return C.CBytes(payload), C.ushort(error_SUCCESS)
}

func main() {}
