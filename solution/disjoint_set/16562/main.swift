# Authored by : iyeaaa
# Co-authored by : -
# Link : http://boj.kr/a5ff34cf2dc845f19b2742d7ab1bc7f9

var input = readLine()!.split{$0==" "}.map{Int(String($0))!}
let (n, m) = (input[0], input[1]); var k = input[2]
let cost = [0] + readLine()!.split{$0==" "}.map{Int(String($0))!}
var friend = Array(0...n)
var minCost = cost

for _ in 0..<m {
    input = readLine()!.split{$0==" "}.map{Int(String($0))!}
    merge(input[0], input[1])
}

var sum = 0
for i in 1...n {
    if isRoot(i) {
        sum += minCost[i]
        k -= minCost[i]
    }
}

print( k < 0 ? "Oh no" : sum )

func find(_ x: Int) -> Int {
    if x == friend[x] { return x }
    friend[x] = find(friend[x])
    return friend[x]
}
func merge(_ x: Int, _ y: Int) {
    let (x, y) = (find(x), find(y))
    if x == y { return }
    friend[x] = y
    if minCost[x] > minCost[y] { minCost[x] = minCost[y] }
    else { minCost[y] = minCost[x] }
}
func isUnion(_ x: Int, _ y: Int) -> Bool {
    find(x) == find(y)
}
func isRoot(_ x: Int) -> Bool {
    x == friend[x]
}
