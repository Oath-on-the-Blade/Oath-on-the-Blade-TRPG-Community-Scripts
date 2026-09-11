# 《三盞閘燈不能同時熄》關連樹目錄

> 關係索引文檔；不是資料夾、不是固定戰役。

- **根任務**：《三盞閘燈不能同時熄》
- **根 `script_id`**：`ootb-hard-sluice-three-lamps-001`

## 節點

| 劇本 | `script_id` | 直接來源 | 關連定位 | 前作要求 |
|---|---|---|---|---|
| 《三盞閘燈不能同時熄》 | `ootb-hard-sluice-three-lamps-001` | — | 根任務 | 無 |
| 《新閘六道泄洪槽只有五道見過水》 | `ootb-xinzha-liudao-xiehongcao` | 《三盞閘燈不能同時熄》 | 後續／水閘制度與責任承接 | 非必要；可獨立運行 |
| 《柳堤三份驗水簿有一份少了夜班押字》 | `ootb-linked-liudi-three-water-ledgers-night-signature-001` | 《新閘六道泄洪槽只有五道見過水》 | 後續／新閘驗收後的維護責任鏈延伸 | 非必要；可獨立運行 |
| 《柳堤四面巡渠牌有一面換了釘位》 | `ootb-linked-liudi-four-canal-markers-renailed-001` | 《柳堤三份驗水簿有一份少了夜班押字》 | 後續／常態維護責任鏈的水路標識延伸 | 非必要；可獨立運行 |
| 《柳堤五根量水樁有一根早了一寸》 | `ootb-linked-liudi-five-water-gauges-one-inch-early-001` | 《柳堤四面巡渠牌有一面換了釘位》 | 後續／巡護制度後的量水校準與責任延伸 | 非必要；可獨立運行 |
| 《柳堤六枚午汛牌有一枚先翻了面》 | `ootb-linked-liudi-six-flood-boards-one-turned-early-001` | 《柳堤五根量水樁有一根早了一寸》 | 後續／量水校準後的午汛通報與放水責任延伸 | 非必要；可獨立運行 |

## 關連圖

```text
三盞閘燈不能同時熄
└─→ 新閘六道泄洪槽只有五道見過水
    └─→ 柳堤三份驗水簿有一份少了夜班押字
        └─→ 柳堤四面巡渠牌有一面換了釘位
            └─→ 柳堤五根量水樁有一根早了一寸
                └─→ 柳堤六枚午汛牌有一枚先翻了面
```

## 共同背景與 state

- 前作的閘務事故可造成地方對放水程序、走私與證物保存的不同警覺，但後作本身的客觀事故原因不得由前作 ending 決定。
- 《新閘六道泄洪槽只有五道見過水》可讀取 `sluice-held-all`、`sluice-held-ship-gone`、`sluice-evidence-over-market`、`sluice-people-over-proof`、`sluice-collusion`、`sluice-abandon` 或無前作紀錄；這些只改變開場取得資料、信任與程序成本。
- 《柳堤三份驗水簿有一份少了夜班押字》只承接新閘已進入常態驗水／維護制度及前作實際保存的官面信任／證物程序狀態；不把前作 NPC、私窖、石塞或物件升格為必要前置。無前作紀錄時使用自身完整獨立基線。
- 《柳堤三份驗水簿有一份少了夜班押字》新增 state：`liudi-maintenance-chain-cleared`、`liudi-water-safe-records-pending`、`liudi-wrong-blame`、`liudi-records-destroyed`、`liudi-abandoned`；各 state 只保存該篇實際成立的維護責任與證物結果，不反向改寫更早劇本。
- 《柳堤四面巡渠牌有一面換了釘位》只承接柳堤常態巡護制度與上述可選 state；前作 NPC、麻繩、三簿原件及物權均不是必要前置。前作 state 只改變本篇准入、信任或現有記錄條件，不改寫本篇固定的重釘、私開支堰與責任真相。
- 《柳堤四面巡渠牌有一面換了釘位》新增 state：`liudi-marker-chain-restored`、`liudi-marker-safe-liability-open`、`liudi-marker-false-blame`、`liudi-marker-evidence-lost`、`liudi-marker-abandoned`。
- 《柳堤五根量水樁有一根早了一寸》只承接柳堤巡渠牌、巡水簿與常態責任鏈已成為日常制度，以及上述可選 `liudi-marker-*` state。前作 NPC、巡渠牌原件、支堰鑰與前作證物都不是必要前置；前作 state 只改變本篇程序、准入、信任與可用記錄，不改寫本篇固定的第三樁工程失準、第五樁假痕及真實水位。
- 《柳堤五根量水樁有一根早了一寸》新增 state：`liudi-gauge-truth-calibrated`、`liudi-gauge-safe-liability-open`、`liudi-gauge-wrong-blame`、`liudi-gauge-evidence-lost`、`liudi-gauge-abandoned`。
- 《柳堤六枚午汛牌有一枚先翻了面》只承接量水、巡水與午汛通報已成為柳堤常態責任鏈，以及上述可選 `liudi-gauge-*` state。前作 NPC、五根量水樁原件與前作證物均不是必要前置；前作 state 只改變程序、准入、信任與可用舊記錄，不改寫本篇固定的誤聽錯牌、前日擅開及今日守水命令。
- 《柳堤六枚午汛牌有一枚先翻了面》新增 state：`liudi-floodboard-chain-cleared`、`liudi-floodboard-safe-liability-open`、`liudi-floodboard-wrong-blame`、`liudi-floodboard-evidence-lost`、`liudi-floodboard-abandoned`。

## branch-specific state

- `liudi-maintenance-chain-cleared`：完整維護責任鏈成立；後篇可據此降低程序准入成本。
- `liudi-water-safe-records-pending`：先保水工安全、記錄責任待續查；後篇原件採較嚴格保管。
- `liudi-wrong-blame`：留下可歸因的錯誤歸責；後篇普通渠役對角色口頭結論較保守。
- `liudi-records-destroyed`：記錄鏈不可使用；後篇不得補造文件。
- `liudi-abandoned`：由地方自行維持最低限度巡護；後篇無既有程序信用。
- `liudi-marker-chain-restored`：巡渠標識與責任鏈完整恢復；量水樁篇開場可直接取得最近七日抄錄副本。
- `liudi-marker-safe-liability-open`：水工安全已處理但責任未結；量水樁篇原件採桌面查驗與簽押抄本。
- `liudi-marker-false-blame`：前篇留下錯誤歸責；量水樁篇普通堤役較戒備，但不封鎖必要資訊。
- `liudi-marker-evidence-lost`：前篇證物不可用；量水樁篇不得補造，只用本篇五樁、底座、石階與當日簿冊。
- `liudi-marker-abandoned`：前篇程序信用不足；量水樁篇仍以自身完整基線運行。
- `liudi-gauge-truth-calibrated`：量水真相與校準責任完整釐清；午汛牌篇可直接取得今日正本與六點回牌時刻抄本。
- `liudi-gauge-safe-liability-open`：先保水工安全、責任未結；午汛牌篇原始值守簿採桌面查驗與簽押抄本。
- `liudi-gauge-wrong-blame`：前篇留下錯誤歸責；午汛牌篇普通堤役對外部結論較戒備。
- `liudi-gauge-evidence-lost`：前篇證物不可用；午汛牌篇不得補造，只使用本篇自身證據鏈。
- `liudi-gauge-abandoned`：前篇程序信用不足；午汛牌篇仍以自身完整基線運行。
- `liudi-floodboard-chain-cleared`、`liudi-floodboard-safe-liability-open`、`liudi-floodboard-wrong-blame`、`liudi-floodboard-evidence-lost`、`liudi-floodboard-abandoned`：只保存《柳堤六枚午汛牌有一枚先翻了面》的各主要結果，供未來同樹節點按正文條件讀取。

## 可累積 state

- 只要來源正文沒有明列互斥，較早節點的制度／信任狀態可與較後節點的本地事件結果共同保存。
- `liudi-marker-chain-restored` 可與不衝突的更早水閘制度 state 同時成立；它不覆寫更早 ending。
- 任一 `liudi-gauge-*` 結果可與不衝突的較早制度／信任 state 共同保存，不覆寫前篇結果。
- 任一 `liudi-floodboard-*` 結果可與不衝突的較早制度／信任 state 共同保存，不覆寫前篇結果。

## 互斥 state

- 同一次《柳堤三份驗水簿有一份少了夜班押字》運行的五個主要 ending state 彼此按該篇實際 ending 保存。
- 同一次《柳堤四面巡渠牌有一面換了釘位》運行的五個主要 ending state 彼此按該篇實際 ending 保存。
- 同一次《柳堤五根量水樁有一根早了一寸》運行的五個主要 ending state 彼此按該篇實際 ending 保存。
- 同一次《柳堤六枚午汛牌有一枚先翻了面》運行的五個主要 ending state 彼此按該篇實際 ending 保存。
- 不因不同劇本位於同一路徑便自動互斥。

## 主要 ending／state → 後續映射

- 《柳堤三份驗水簿有一份少了夜班押字》的五個主要 state 均可進入《柳堤四面巡渠牌有一面換了釘位》；前作非必要，無前作紀錄也可進入。
- 《柳堤四面巡渠牌有一面換了釘位》的五個主要 state 均可進入《柳堤五根量水樁有一根早了一寸》；前作非必要，無前作紀錄也可進入。
- 《柳堤五根量水樁有一根早了一寸》的五個主要 state 均可進入《柳堤六枚午汛牌有一枚先翻了面》；前作非必要，無前作紀錄也可進入。
- 進入新篇時，各前作 state 只依新篇正文改變資料准入、見證要求、信任或可用舊記錄；不改變新篇固定真相。
- 《柳堤六枚午汛牌有一枚先翻了面》的五個主要 ending 目前不預先指定特定後續；未來可由同一 state 開啟一篇或多篇同樹後續，只要來源條件相容。

## 多來源條件

- 目前最新節點《柳堤六枚午汛牌有一枚先翻了面》只有一個直接來源，無 `AND`／`OR` 多來源條件。
- 未來若新增匯流節點，必須在劇本正文與本目錄同步列明所有直接來源及 `AND`／`OR`／互斥邏輯。

## 維護

- 新增本樹分支時可由同一 ending 開啟多篇後續；除非正文建立明確互斥 state，否則不得因「同源分支」自動視為二選一。
- 本目錄只索引關係與 state，不取代任何劇本正文，也不創造正文未存在的新正史。
- 劇本檔維持 repo 原路徑，不因樹成員資格搬動、複製或建立同名資料夾。