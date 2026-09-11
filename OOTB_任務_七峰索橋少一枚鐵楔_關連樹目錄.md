# 《七峰索橋少一枚鐵楔》關連樹目錄

> 關係索引文檔。各劇本正文是客觀真相與 state 的權威來源。

- 根任務：《七峰索橋少一枚鐵楔》
- 根 `script_id`：`ootb-random-tianyue-wedge-001`

## 本樹最新直接邊

`《南橋試坡棚四張載重籤有一張先寫了通過》 → 《南橋放車門三塊驗載牌有一塊掛在空鉤上》 → 《南橋放車門兩本出門簿有一本少了半頁》`

## 最新節點

| 劇本 | `script_id` | 直接來源 | 前作要求 |
|---|---|---|---|
| 《南橋放車門兩本出門簿有一本少了半頁》 | `ootb-linked-tianyue-southbridge-gate-ledger-001` | 《南橋放車門三塊驗載牌有一塊掛在空鉤上》 | 非必要 |

## 共同背景基線
- 天嶽七峰外圍的山路、橋索、貨務、車具、鐵作、封件與交接責任構成同一地方運作背景。
- 後作只承接直接來源已保存的制度與 state；每篇新事件的責任、人物、物件與失誤以本篇正文為準。
- 《南橋放車門三塊驗載牌有一塊掛在空鉤上》只承接 `southbridge_load_slip_*` overlay。
- 《南橋放車門兩本出門簿有一本少了半頁》只承接 `southbridge_release_tag_*` overlay；舊新兩冊、三車轉抄、撕角留樣、黏頁與缺頁均是新事件。
- 各節點不要求相同建議等級、R、規模或難度。

## Branch／state 路由
- 《南橋放車門三塊驗載牌有一塊掛在空鉤上》可建立 `southbridge_release_tag_chain_restored`、`southbridge_release_tag_rehandoff_completed`、`southbridge_release_tag_safe_hold`、`southbridge_release_tag_incident`、`southbridge_release_tag_unresolved`、`southbridge_release_tag_seized`。
- 《南橋放車門兩本出門簿有一本少了半頁》只讀上述 `southbridge_release_tag_*`；它們只改調閱合作、封存意願、正式取樣見證與催放時點，不改本篇核心事件。可建立 `southbridge_gate_ledger_chain_restored`、`southbridge_gate_ledger_dual_procedure_retired`、`southbridge_gate_ledger_safe_hold`、`southbridge_gate_ledger_incident`、`southbridge_gate_ledger_unresolved`、`southbridge_gate_ledger_seized`。

## ending／state → 後續
- 《南橋放車門三塊驗載牌有一塊掛在空鉤上》的任何 ending 或無紀錄都可進《南橋放車門兩本出門簿有一本少了半頁》；只有實際存在的 `southbridge_release_tag_*` 形成 overlay，前作不是必要前置。
- `southbridge_gate_ledger_chain_restored=true`：舊簿—新簿—留樣—當班車次換冊鏈已復核。
- `southbridge_gate_ledger_dual_procedure_retired=true`：同頁重複採用兩套換冊做法的程序已停用。
- `southbridge_gate_ledger_safe_hold=true`：兩冊與留樣已安全封存，缺頁責任仍可續查。
- `southbridge_gate_ledger_incident`、`southbridge_gate_ledger_unresolved`、`southbridge_gate_ledger_seized` 依正文保存相應狀態。
- 本次沒有新增互斥 state。

## 既有節點保留原則
本次同步不改變此前已發布節點正文、直接來源、既有 state 語義或可達性；如需查既有節點，以各劇本正文為準。本索引不創造新的前置或正史。

## 維護
新增、刪除或改變直接邊、ending/state 路由或共同背景時同步更新本檔。劇本檔維持原路徑，不建立同名資料夾、不搬檔。