import endgame

allboards= ['..wwwww.b.wwbw..bbwbbwwwbwbbbwwwbbwbbwwwbbbwbwww..bbwbw....bbbbw',
"wbbw.b...wwbwww.wwwwbwwwwwwbwbbbwwwwbwb.wwwwwbbb..wwbbb..wwwww..",
"..w.bb.bw.wbbbbbwwwwbbbbwbwwwwbbwbbbwwbwwwbbbbbww.wbbbbw......bw",
"bwwwwww..bwwwww..bbbwwww.bbbbbww.bbbbwww.bbbbbww..bbbbw...bbbbbw",
"b.wbw....bwwww.bbbbbbbbbbbbbbbbbbbwbbbbbbbbwwbbbb.wwww....w.bbbb",
"..bwb..b.bbwwwwwbbbwbbwbbwwbbbwbbwwwbwbbb.wwwwbbb.wwwb.b...wbbb.",
"...bwwbb..bbbwwb.bbbbbwwbbwbbbb.bbbwbbbb.bbbwwbb..bbbbbb..bbbbwb",
"..bbbbwb..bbbwbb.bbwwbbbwwwwbbbb.wwbbbbb.wwbbwbb.bbwww...bwwwww.",
"..b.....wwbb.b..wwwbbbbbbwwwbbwwbbwbbwwwbbbwwwwwbwbbwb..bwwwwwww",
"b.w.b...bb.bbw.wbbbbbbwwbbbbbwwwbwwwwwwwbwbwwww.bbwwww.b..wwwww.",
"b..b....b.bbbb.bbbwwwwbbbbbbwbbbbwbwbbbbbwbwbwbbbwwwww..bwwwww..",
"wbbb.ww.wbbbbw.bwbbwwb.bwbbwwbwbwwbwwww.wwbwwwwwwbwwww....ww..w.",
"bbbbbbb...wwww.bbbbbbwwb.bwbwwwbbbbwwwwb.bbbwwwb..wwbww...wwwww.",
"b.w.b...bb.bbw.wbbbbbbwwbbbbbwwwbwwwwwwwbwbwwww.bbwwww.b..wwwww.",
"bbbbbbb...wwww.bbbbbbwwb.bwbwwwbbbbwwwwb.bbbwwwb..wwbww...wwwww.",
"b..b..w.bbbbbw.bbwbwwwbbbwbbwbbbbwbwbbbbbwbbbwbbbbbbww..b.b.ww..",
"b..b....b.bbbb.bbbwwwwbbbbbbwbbbbwbwbbbbbwbwbwbbbwwwww..bwwwww..",
"...bbbb...bbbb.wbbbbbww.wbwbwww.wbbbbwwwbbbbbbww.bbbbbbw.wwwwww.",
"..bbb.....bbbw.wwwwwbwwwbwwbbbbwwwbwwbbw.bwwbwbwb.wwbbbw..wwwwbw",
"w..bbbb.bbbbbbb.wbwbwwbbwwbbwbbbwwbbwbbbw.wwwwbb..wwww.b..wwww..",
"..bbbbb.wwbbbbb..wwbbbbwbbwwwbbwbbwwwbbwbbbbbwbww.wwwwww.....w.w",
".bbb....w.bbbb.wwbbbbbbbwbbwbbbbwbwbwwbbwwbbbbwbw.bbbwww...bww.w",
"..wwwww.bbwwww.bbbbwwwbbbwbbwbwbbwbbwbbbbbwbbbbbb.wwww......www.",
"w..bbb..bbbbbb..wbwbwbbbwbbwwbbbwbwbwbbbwbbwwwbb.bwwww.b..wwww..",
".bbbbbbb..wwbwb.wwwwwbww.wbwbwwb.bwbbwbb.wbbbbbb...bbbbb..wwwwww",
"..bbbbbw..bbbbww..bbbwbw..bbwbbw.wbwwbbwwwbbwwwwwwbbbb.bbbbbbb..",
".wwwww...wwbbbb.wwwwbbbbwwwwbwb.wwwwwww.wbwwwwwwbbbwww..wwww..w.",
"b.w.b...bb.bbb..bbbwwwwwbbbbbwwwbwbbwwbwbbwwbwwwbwwwwwwww....wbw",
"...bbbb...bbbb.wbbbbbww.wbwbwww.wbbbbwwwbbbbbbww.bbbbbbw.wwwwww.",
".wbbbb.w..bbbb.w.wbwwwbw.bbwwwww.bbwwwbw.bwbwbww.bbbbww.wbwwwww.",
"..wbbw.w..wwwwwbwwwwwwbbwwwbwbwbwwbwbwwbwbbbwbbbw.bbbbbb..bb....",
"..bbbbb..bbbbbbbbbbwbbbbwbbbwbbbbbbbbwbb.bbbwww..bbbbwww....bbw.",
"..w..bww...wbbbb..wwbbbwbbbbbbwwbbbbwbwwbwbbwwwwbbwwwww.bbbbb.w.",
".wwwww..b.wbbw.w.bbwwbwwwwbbwwb.wwwbwwbbwwbwbwbb..bbwbb...bbbbbb",
"....w.....wwww.wwwwwbbbbwwwbwbbbwwwbwwbbwwbwwbwb.bbbbbbw.wwwwwww",
".ww.b.....wwbb..wbbwwbbbwbbbwwbbwbbbbbwbwbbbbwbb.bbbwb.b.bbbbbbb",
"..wbbbbww.bbwwwwwbbbwwwwwbbwwbwwwwwwwwwww.wbbwwww.w..www...bbb..",
".wbbbb.w..bbbb.w.wbwwwbw.bbwwwww.bbwwwbw.bwbwbww.bbbbww.wbwwwww.",
"..bbbb..w.bww...wwbbww..wbbwbwwwwbbbwwwwwbbbbwbw.bbwbbbw.bbbbbbw",
".bb.w....bbbww.bwbwbbwbbwwbwwbbbwwbwwwb.wwwbbwww.wwwwwww..bwwww.",
".....w....wwwwwwbbwbbbwb.bwwwwwbbbbwwbwbbbwbbwbbbbbbbbbbwbbbbb..",
"w..bww..bwwbbbbbbbbwbbbbbbbbwbbb..bwwwb...wwbwww.wwwwwww.wwwwww.",
"wwwwwbw...wwwww.bbwbbbbb.bbwwbbbbbbbbbbb.bwwwbbbb.wwww....wwwww.",
"..w.wb..wwbwww..wwbbwbw.wbbwbbw.wbbbwbwwwwbwwwbwwbbbbbbwb.bb..bw",
"..wbbw..wwwbbbbbwwbbbbbbwwwbbbwbwwwbwwww.wbbwb.w.bbbbw...b.wwww.",
"..wbbb.....b.bwwwwbbwbwwwwbbwwww.wbwwbww.wwbbwwb.wwwwwwb.wwwwwww",
"b.wwwww.bbwwwwb.bwbwwbbb.bwbbwbb.wbwbbbbw.bwbbbw...wwbbw..bw.wbw",
"..bwww....bbbb...wbwbb.wwwbwwwwwwwbbwbwwwwbbbwbwwwwbbbbw..wbbbbw",
"bbbbbb...bwbbbbbbbbwwbbwbbwbbbww.bwbbbw..bwbwbw...wwbwb...wwwwwb",
"w.w.....w.wwwb..wwwwbwwbbwbbbwwbbwbwwbwbbbwwbbbbbwwbww.bwwwwww..",
"....b.wb..bbbbbb..bbbbbb..bbbbw.wwbbbwwwwbbbbwwwbbbwwwwwbwwwwwww",
".bbbbbb.b.bbbb.bbbwwwwbbbbwwbwwbbbwbwbwb.wbwwwbbw.wwww.b...wbw..",
".wwwwww...wbbw..w.bwwbw..bbbwbwwbbbwbbwwbbwbbbbw.wbbbbbw..wbbbbw",
"..wbbw...wwwwwbbbbwbwwwbbbbwbbwbbbbbbbwbbbbbbwbb..bbbb.b..bbbb..",
"..wbbw..wwwbbbbbwwbbbbbbwwwbbbwbwwwbwwww.wbbwb.w.bbbbw...b.wwww.",
"b..www...bwwwwwwbwbbbbwwbwbbbwbwbbbbbbbwbbbbbbbwb..bbbbw...w..bw",
".b.www....bbbb...wwbbb.wwwwwbwwwwwwbwbwwwwbbbwbwwwwbbbbw..wbbbbw",
".bbbbb...wwwwbbbwwwbwbb.bwbwwbbwbbwbwbbwbbbbbbww...bbbww....wbbw",
"..bbbb.b..bwbbb.bbbbbbbbbbbbbbbbbbbbwbbbwbbbbbbb..bbbb...wwwwww.",
".wbw.....bbbwb..bwbwbw...wwwwwwbwwwwbwbbwwwwwbbbbwbwbbbb.bwwwwwb",
".wwwww....wbbw..bbbbbww.bbbwbww.bbbwwbwwbbbbwbww.wbbbbbw..bbbbbw",
"wwwbbbbwbbbbbbbwwbwbwwww.wbwwwbwwwwwwbwwb.bbbwww...bbww......bw.",
".b.wwww...bbbw...wwbwb.wwwwwbbb.wwwbwbbbwwbbbwbbwwwbbbbb..wbbbbw",
"..b.b.w.w.bbbb.b.bbbwbbbbbwbbwbbbwwwbwwbbwwwwbwbb.wwwwbb..wwww.b",
".wwwww...bbbbw.bbwbwwwbbbwwbwbbbbwbwbbb.wwwbwb.w.wwbbw...wwwwww.",
"..bbbw...bbbbb..bwwbbbbbbbwwbbbbbwbbwwwwbbwbwwwwb.bwbww..b.wwww.",
"..bbbbb.w.bbwb..wbbwbww.bbbbwww.bwwwwww.bwwwwwwwb.wwwww..bwwwwww",
"..w.wb....wwwb.wbbwwwbwwbwwwbwwwbbbwwbwwwwwbwwbw..wwbbbb..wwwwww",
"..bbbbbbw.bbbb.bwwbwbwwbwbwbwwwbwwbbwbwbwwwwwwbb...w.bwb....bbww",
"...bw....bbwwb.bwwbwwbbbwwwbwbbb.wwbbbbbbwwbbbwb..wwwwwb.bwwwbbb",
"..wbwwwbwbbbbwwbwbbbwbwbwwwwbwwbwbwbwbwbwwbwwwbbw..bww.b.....w..",
"..bbw..w..bwwwbbwwbbwwwbwbbwwwwwwbwwwwwwwwwwwww.wbwww...wwwwww..",
"..wwwww..bbbww.wbbbwwwwwbbbwwwbwbbwbwwwwbwbbbwwwbbbbbb..b.b...b.",
".bbbbbb...bbwb..wwbwbwwbwwwbwwwwwwwwbbwb.wwwbbw..wwbwww...bwwwwb",
".bbb..wwb.bwbwbbwbwbwwbbwbbwwwbwwbwwbw..wwwwwww.wbwww...wwwwww..",
"..wwww....wwwwb.bbwwwbbwbwwwbwbwwwwwwwbbbbbwbwbw.bbbww..bwwwww..",
".bbbbbbb.bbw.wb.wbbwwbwbwbbbbw.wwbwbbww.wbbwwb..wbbbbbb..wwwww..",
"wbbbwb...bbbbw..wbwwwwwbwwbwwwbbwwwwwbwbwwwbwwbb..wbww.b..wwww..",
"..wbb...bbwbbb..bbbwwwbwbbwbbbbbbbbwbwbb.bbbwbbbwwbwbbb..wwbbw..",
"bbbbbbb..bwwwb.w.wbbbbbw.wwbbwbw.wwwwbbw..wwbwbw...wbbbw.wwwwwww",
"b.w..w.b.bwwwwww.bbwbbwwbbbbbwbwwbwwwwww..bbbbbw..bbbbbw..bbbbbw",
".bbbbb..b.bbbbw.bbwbbwb.bwwwbbbbbwwbwbbwbwbbbbb.bbbwww..bb...www",
"wwwwwww..wbbbw.w.wwbbbbw.wbwbbbwwwwwbwwwb.wwbwbw..wwbbbw...wb.bw",
".bbbwww..bbwwwwwwbwwwwwwwwbbbwwwwbwbbbwwwwbbwbbbw.bbb.....bbw...",
"wwwwwww..wbbbw.w.wwbbbbw.wbwbbbwwwwwbwwwb.wwbwbw..wwbbbw...wb.bw",
"..w.wb..w.wwww...wbbwwbb.bwbbbwbwbbbbwwbwwwbbbbbw.bwbbbb.bbbbbwb",
"..ww....w.www...wwwbbwbbwwbbbbwbwbwwbbwwbbwwwbbbb.bwwwbb.bbbbwwb",
".wwwww..b.wbbw..bwbwbbw.bbbwbwwwbbbbwwwwbbbbww.b.bbbbbw...wwwwww",
"...wbb..bb.wbbb.bbbbwwwwbbbbbwwwbbwbwwww.wbwbwwww.bbbb...wwwwwww",
"..wwww.bbbwwwwb.bbbwwbwwwbbbbwbbbbbbbww.bbbwbw.w.bbw.w...bbb.www",
"w.wbbbbw.wbbbbb.bbwbbwb..bwwbwbwbbbwbbbwwbbbbbbw..bbbbb....wwww.",
"..bb.b....bbbb.bwwwwwwbb.bwbwbbbbbbbbbbbbbbbbbwbb.wwwwwb..bwwwwb",
"..wwwb..b.wwbb..bbbbwbbbbbbwbbbbbbwbwwbb.bwbwbwww.bbbbw...wbbbbw",
"bbbbbw..bwwb.w..bbbwww..bbwwwww.bwwbwbw.bwbbwwbww.bbwbb..wwbbbbw",
"..bbbbb.w.bbbb.bwbbbbbbbwbbbbbwbwbwbwww.b.wwwww..bwwww...bbbbbbb",
"w.wbbbbw.wbbbbb.bbwbbwb..bwwbwbwbbbwbbbwwbbbbbbw..bbbbb....wwww.",
"..wbbbbw..bwwwwwwbwbwbwwbbbwwwbww.wbwbww.wbwbwww..bbwww..bbbbw..",
"..bbbb....bbbb..wwwwwbwbwwwwwwbbwwwbwwbbwwbwbwb.wbbbbbbw...bbbbw",
".bbbbbb.wwwwbw..wwwbwbw.wbwwwwb.wbbbbbbbwwwwwww.w.wbww....wbwwww",
".wwwwww...bbbb..b.bbwbbbwwbbwbb.bwbbwbb.bwwbbbb.wwwwbwb..bbbbbbb",
"wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww..",
"wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwb.",
"wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwbw..",
"wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwbww.",
"wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwbw...",
"wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwbwbw....",
"bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbwbw...",
"bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbwb...",
"bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbwb..",
"bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbwb.",
"bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbwbbbbbbbwbbbbbwb.",
"wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwbwwwwwwwbwwwwbbb." ]


nb_try = len(allboards)

for i in range(nb_try):
    bds = allboards[i]
    print (bds, ' => ', endgame.solve(bds))
             