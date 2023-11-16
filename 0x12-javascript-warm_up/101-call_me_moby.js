#!/usr/bin/node

const callMeMoby = function (x, theFunction) {
    let i;

    for (i = 0; i < x; i++) {
        theFunction();
    }
}
exports.callMeMoby = callMeMoby
