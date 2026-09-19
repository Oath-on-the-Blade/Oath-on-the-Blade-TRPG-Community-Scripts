# 《白蘆河七座浮橋有兩座在夜汛前鬆了主纜》關連樹目錄

> 作者／維護者用關係索引；不是可玩劇本。個別劇本正文為運行權威，本檔不得覆寫正文。

## 穩定根
- 根任務：《白蘆河七座浮橋有兩座在夜汛前鬆了主纜》
- 根檔案：`OOTB_任務_白蘆河七座浮橋有兩座在夜汛前鬆了主纜.md`
- 根 `script_id`：`ootb_highrisk_bailu_two_pontoon_cables`

## 節點
| 節點 | 檔案／script_id | 直接來源 | 關連 | 必要前置 |
|---|---|---|---|---|
| A｜白蘆河七座浮橋有兩座在夜汛前鬆了主纜 | `OOTB_任務_白蘆河七座浮橋有兩座在夜汛前鬆了主纜.md`／`ootb_highrisk_bailu_two_pontoon_cables` | 無 | 根 | 無 |
| B｜白蘆河三批補橋木有一批先到了空碼頭 | `OOTB_任務_白蘆河三批補橋木有一批先到了空碼頭.md`／`ootb_related_bailu_repair_timber_empty_wharf` | A | 後傳 | A 的 `END-01 OR END-02 OR END-03` |
| C｜白蘆河五冊驗料簿有兩冊在同日換了新戳 | `OOTB_任務_白蘆河五冊驗料簿有兩冊在同日換了新戳.md`／`ootb_related_bailu_five_inspection_ledgers_new_seals` | A + B | 後傳／匯流 | `(A:END-01 OR END-02 OR END-03) AND (B:BAILU-R1 OR R2 OR R3 OR R4 OR R5)` |

## 關連圖
```text
A:END-01 ─┐
A:END-02 ─┼→ B ─┐
A:END-03 ─┘      ├→ C
A:END-01/02/03 ──┘

A:END-04 / END-05 → 不開啟 B 或 C
```

## 共同背景基線
- 承泰二十一年，江南道澄州外白蘆河支渠、七座浮橋與兩岸小聚落均為根任務建立的地方事實。
- 根任務夜汛中，橋三問題源於岸基位移；橋六曾被人為放長；人流、船流、漂木與洪峰曾形成同一危機窗口。
- 後作不得把兩橋事故改寫成同一幕後主使，也不得無聲改寫根任務已結算的橋損、傷亡、物權或 NPC 責任。
- B 建立夜汛後三批補橋木、柳灣臨碼頭、舊戳／改卸單與修橋排程等地方事實；其責任、物權與證物狀態以 B 的正式結算為準。
- C 建立河務棚驗料房、舊紙庫及兩冊同日換新戳事件；其中橋三正常補簽與橋六違規改頁是兩條不同因果，不得合併成 B 的同一偽造行為。
- 根任務與後作 NPC 的姓名、存活、職務與已公開資訊按該桌存檔保存；跨篇引用既有 NPC 時沿用 `NPC#前作編號@前作劇名`。

## branch-specific state
- `A:END-01`：至少一座受威脅浮橋安全保留；撤離與船隊危機已受控；事故原因有可核驗說明。
- `A:END-02`：至少一座危橋被封閉或拆除並待重建；人員與船隊安全。
- `A:END-03`：人命大致保住，但橋路或糧運有重大損失。
- `A:END-04`：嚴重混亂、傷亡或兩橋同失；不開啟 B、C。
- `A:END-05`：角色放棄根任務；不開啟 B、C。

## 可累積 state
B 結算後可保存：
- `BAILU_repair_timber = recovered / unavailable / lost / unknown`
- `BAILU_forged_release = evidenced / suspected / unresolved / unknown`
- `BAILU_repair_schedule = on_track / delayed / unknown`
- 木料保管位置、偽單／舊戳證物狀態及 B 的 NPC 動態狀態。

C 結算後另保存：
- `BAILU_ledger_integrity = preserved / partial_or_lost`
- `BAILU_bridge6_liability = evidenced / unresolved`
- 五冊驗料簿、停戳登記、覆簽與量尺的實際保管／證物狀態。

以上可與 A 的橋損、NPC 狀態及社會名譽結果並存；後作不得用新 state 洗掉舊篇差異。

## 互斥 state
- 同一桌同一次 B 結算中，`BAILU_repair_timber`、`BAILU_forged_release`、`BAILU_repair_schedule` 各只能有一個最終值。
- 同一桌同一次 C 結算中，`BAILU_ledger_integrity` 與 `BAILU_bridge6_liability` 各只能有一個最終值。

## ending／state → 後續映射
| 來源 | 可達節點／結果 |
|---|---|
| A `END-01` | B；以加固／更換受損構件為修繕背景；B 完成後可與其結果共同開啟 C |
| A `END-02` | B；以至少一橋重建為修繕背景；B 完成後可與其結果共同開啟 C |
| A `END-03` | B；按實際橋路／糧運損失決定最急材料位置；B 完成後可與其結果共同開啟 C |
| A `END-04` | B、C 不可達 |
| A `END-05` | B、C 不可達 |
| B `BAILU-R1` | 與合資格 A ending 共同開啟 C；保存三項 B state |
| B `BAILU-R2` | 與合資格 A ending 共同開啟 C；保存三項 B state |
| B `BAILU-R3` | 與合資格 A ending 共同開啟 C；保存三項 B state |
| B `BAILU-R4` | 與合資格 A ending 共同開啟 C；保存三項 B state |
| B `BAILU-R5` | 與合資格 A ending 共同開啟 C；按實際狀態保存，不補寫未知答案 |
| C `BAILU-L1` | 目前無既定後續；保存兩項 C state |
| C `BAILU-L2` | 目前無既定後續；保存兩項 C state |
| C `BAILU-L3` | 目前無既定後續；保存兩項 C state |

## 多來源條件
- B 只有 A 一個直接來源，前置為 `END-01 OR END-02 OR END-03`。
- C 同時直接依賴 A 的橋損／已公開責任與 B 的修橋材料、偽單證物、排程 state，因此 A、B 都是直接來源。條件為：`(A:END-01 OR END-02 OR END-03) AND (B:BAILU-R1 OR BAILU-R2 OR BAILU-R3 OR BAILU-R4 OR BAILU-R5)`。
- C 讀取 B 的 state 時只按已結算值分流；`unknown / unresolved` 保持未知，不由 C 補成既定答案。

## 維護註記
- B 的木料、偽單與舊戳物權以 B 正文為準，不因成為跨篇 state 而變成玩家資產。
- C 的驗料簿、停戳登記、覆簽與量尺均屬公務／工程證物；物權與保管依 C 正文。
- 若未來節點需要 A、B 或 C 的 NPC，必須回讀來源全文及已知後續狀態；不能由本索引生成新口供。
- 若未來新增節點同時依賴多個既有節點的劇本專用資料，所有實際來源都應列為直接來源並明列 AND／OR／互斥條件。
- 本樹不得與其他一般關連樹建立直接劇本專用關連。
