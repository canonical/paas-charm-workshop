
var express = require('express');
var router = express.Router();

/* GET users listing. */
router.get('/:num', function (req, res, next) {
    let n = parseInt(req.params.num, 10);

    if (n < 0) {
        return res.status(400).json({ error: "Invalid input" });
    }

    const fib_sequence = [];
    let a = 0, b = 1;

    for (let i = 0; i < n; i++) {
        fib_sequence.push(a);
        [a, b] = [b, a + b];  // Swap a and b
    }

    return res.json({ fibonacci: fib_sequence });

});

module.exports = router;
