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

## 關連圖
```text
A:END-01 ─┐
A:END-02 ─┼→ B
A:END-03 ─┘

A:END-04 / END-05 → 不開啟 B
```

## 共同背景基線
- 承泰二十一年，江南道澄州外白蘆河支渠、七座浮橋與兩岸小聚落均為根任務建立的地方事實。
- 根任務夜汛中，橋三問題源於岸基位移；橋六曾被人為放長；人流、船流、漂木與洪峰曾形成同一危機窗口。
- 後作不得把兩橋事故改寫成同一幕後主使，也不得無聲改寫根任務已結算的橋損、傷亡、物權或 NPC 責任。
- 根任務 NPC 的姓名、存活、職務與已公開資訊按該桌存檔保存；後作引用既有 NPC 時沿用 `NPC#前作編號@前作劇名`。

## branch-specific state
- `A:END-01`：至少一座受威脅浮橋安全保留；撤離與船隊危機已受控；事故原因有可核驗說明。
- `A:END-02`：至少一座危橋被封閉或拆除並待重建；人員與船隊安全。
- `A:END-03`：人命大致保住，但橋路或糧運有重大損失。
- `A:END-04`：嚴重混亂、傷亡或兩橋同失；不開啟 B。
- `A:END-05`：角色放棄根任務；不開啟 B。

## 可累積 state
B 結算後可保存：
- `BAILU_repair_timber = recovered / unavailable / lost / unknown`
- `BAILU_forged_release = evidenced / suspected / unresolved / unknown`
- `BAILU_repair_schedule = on_track / delayed / unknown`
- 木料保管位置、偽單／舊戳證物狀態及 B 的 NPC 動態狀態。

這些 state 可與 A 的橋損、NPC 狀態及社會名譽結果並存；不得用 B 的 state 洗掉 A 的差異。

## 互斥 state
- 同一桌同一次 B 結算中，`BAILU_repair_timber` 只能有一個最終值。
- 同一桌同一次 B 結算中，`BAILU_forged_release` 只能有一個最終值。
- 同一桌同一次 B 結算中，`BAILU_repair_schedule` 只能有一個最終值。

## ending／state → 後續映射
| 來源 | 可達節點／結果 |
|---|---|
| A `END-01` | B；以加固／更換受損構件為修繕背景 |
| A `END-02` | B；以至少一橋重建為修繕背景 |
| A `END-03` | B；按實際橋路／糧運損失決定最急材料位置 |
| A `END-04` | B 不可達 |
| A `END-05` | B 不可達 |
| B `BAILU-R1` | 目前無既定後續；保存三項 B state |
| B `BAILU-R2` | 目前無既定後續；保存三項 B state |
| B `BAILU-R3` | 目前無既定後續；保存三項 B state |
| B `BAILU-R4` | 目前無既定後續；保存三項 B state |
| B `BAILU-R5` | 目前無既定後續；按實際狀態保存，不補寫未知答案 |

## 多來源條件
目前沒有多來源節點。B 只有 A 一個直接來源，前置為 `END-01 OR END-02 OR END-03`。

## 維護註記
- B 的木料、偽單與舊戳物權以 B 正文為準，不因成為跨篇 state 而變成玩家資產。
- 若未來節點需要根任務或 B 的 NPC，必須回讀來源全文及已知後續狀態；不能由本索引生成新口供。
- 若未來新增節點同時依賴 A 與 B 的劇本專用資料，A、B 都應列為直接來源並明列 AND／OR 條件。
- 本樹不得與其他一般關連樹建立直接劇本專用關連。
