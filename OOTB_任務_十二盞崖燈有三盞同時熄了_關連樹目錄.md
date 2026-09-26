# 《十二盞崖燈有三盞同時熄了》關連樹目錄

> 作者／維護者用關係索引；不是可玩劇本，不取代任何節點正文。

## 穩定根
- 根任務：《十二盞崖燈有三盞同時熄了》
- 檔名：`OOTB_任務_十二盞崖燈有三盞同時熄了.md`
- `script_id`: `ootb.highrisk.clifflamps.three-dark.v1`

## 節點
| 節點 | 檔名 | `script_id` | 直接來源 | 關連類型 | 必要前置 |
|---|---|---|---|---|---|
| A | `OOTB_任務_十二盞崖燈有三盞同時熄了.md` | `ootb.highrisk.clifflamps.three-dark.v1` | — | 根 | 否 |
| B | `OOTB_任務_崖燈熄滅後三封急遞只到兩封.md` | `ootb.related.clifflamps.missing-dispatch.v1` | A | 共享事件／平行後果 | 否 |
| C | `OOTB_任務_河棧七張提貨票有一張蓋了兩次印.md` | `ootb.related.clifflamps.double-stamped-ticket.v1` | B | 後傳／共享物件後果 | 否 |

## 關連圖
`A ──共享事件／平行後果──> B ──後傳／共享物件後果──> C`

## 共同背景基線
- 同一夜第七、九、十盞崖燈熄滅，令山路交通與遞送次序短暫失常。
- B 只承接這項已在 A 建立的事件事實；B 不改寫 A 的破壞原因、責任人、驛車／燈夫結果或任何 A 結局。
- A 是否曾實際遊玩，不是 B 的可達條件；無 A 存檔時，B 只使用「燈熄、路亂」基線，不偷指定 A 的任何主要結局為正史。
- C 承接「交通混亂後曾有人抄錄商貨交割資料」這項 B 已建立的物件後果；C 不把 B 的任何人物定罪、生死、原信去向或主要結局升格成全樹正史。
- B 是否曾實際遊玩，不是 C 的可達條件；無 B 存檔時，C 使用「殘抄流出」基線，且不指定 B 的任何 `ending_id`。

## branch-specific state
- A 的各主要 `ending_id`：目前均不改變 B、C 的可達性、核心真相、敵人、DC 或必要線索。若已有存檔，只可把已公開結果作背景消息帶入。
- B：`dispatch_recovered` 與 `dispatch_lost` 互斥；`false_accusation_public` 可與其中任一同時存在。
- C 讀取 B state 的效果：
  - `dispatch_lost=true`：C 的假票取材自失落急遞的抄錄資料；只改河棧掌櫃對票據真偽的初始可信度。
  - `dispatch_recovered=true`：C 的造假者只取得殘抄／口述批號；C 第一次【識字】或【書畫】檢查假票時具有優勢。
  - `false_accusation_public=true`：C 開場可出現遞夫曾被懷疑的舊傳聞；不改 C 的客觀責任。
- C：`duplicate_ticket_exposed`、`duplicate_ticket_redeemed`、`runner_cleared` 均按正文實際結果保存；`duplicate_ticket_exposed` 與 `duplicate_ticket_redeemed` 可同時成立。

## 可累積 state
- `false_accusation_public=true`：B 中曾公開錯誤指控遞夫且未更正；可與急遞去向 state 共存。
- `duplicate_ticket_exposed=true`：C 中雙印假票被可靠證明；可與 `duplicate_ticket_redeemed=true` 同時存在。
- `runner_cleared=true`：C 中受利用跑腿者已由可靠證據洗清；可與其他 C state 共存。

## 互斥 state
- `dispatch_recovered=true` 與 `dispatch_lost=true` 互斥。
- C 目前沒有彼此必然互斥的新增 state；「曾成功領貨」與「之後揭穿假票」可同時成立。

## ending／state → 後續映射
- A：所有主要結局均可進入 B；A 沒有必要前置 gate。
- B `dispatch-recovered` → `dispatch_recovered=true`。
- B `dispatch-saved-copy-only` → `dispatch_lost=true`。
- B `courier-cleared-mastermind-unproven` → 依劇中急遞實際去向寫入 `dispatch_recovered` 或 `dispatch_lost`。
- B 的所有主要結局與無 B 存檔基線均可進入 C；B 不是 C 的必要前置。
- C `ticket-exposed-goods-secured` → `duplicate_ticket_exposed=true`、`duplicate_ticket_redeemed=false`，並依證據決定 `runner_cleared`。
- C `goods-recovered-after-redemption` → `duplicate_ticket_exposed=true`、`duplicate_ticket_redeemed=true`，並依證據決定 `runner_cleared`。
- C `goods-secured-mastermind-unproven` → 依實際證據／放貨狀態保存 `duplicate_ticket_exposed`、`duplicate_ticket_redeemed`、`runner_cleared`。
- C `ticket-redeemed-goods-lost` → `duplicate_ticket_redeemed=true`，其餘依最終證據保存。
- 本目錄目前沒有宣告 C 之後的必要後續；未來新增節點時只能讀取正文已實際建立的 state。

## 多來源條件
目前沒有多來源節點；B 僅直接來源 A，C 僅直接來源 B。

## 維護註記
- 不得把 B 的腳行領班回填成 A 的熄燈主謀或匿名買家；B 明定其只是在交通混亂後臨時起意。
- 不得因 B 存在而改寫 A 的 NPC 生死、責任認定或物件去向。
- 不得把 C 的小貨牙、退職書手、跑腿或河棧掌櫃回填成 A／B 的既有人物；C 明定其造假鏈發生在前作事件後。
- 未來若節點要使用 A、B 或 C 的 NPC，必須回原劇本核對實際 NPC 編號並使用 `NPC#前作編號@前作劇名`。
- 未來若讀取 B 的急遞／抄本物權，必須依 B 的實際 ending/state，不得讓已失落或交回的物件無條件重生。
- 未來若讀取 C 的七匹布、假票、短箋或刻印物證，必須依 C 的實際 ending/state 與 GM 收尾保管記錄，不得由索引創造新物權或新正史。