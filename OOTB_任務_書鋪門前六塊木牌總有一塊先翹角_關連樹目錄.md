# 《書鋪門前六塊木牌總有一塊先翹角》關連樹目錄

> 關係索引文檔；各劇本正文仍是客觀真相與 state 的權威來源。

- **根任務**：《書鋪門前六塊木牌總有一塊先翹角》
- **根 `script_id`**：`ootb_beginner_bookshop_signboard_01`

## 節點與直接關連
| 劇本 | `script_id` | 直接來源 | 關連定位 | 前作要求 |
|---|---|---|---|---|
| 《書鋪門前六塊木牌總有一塊先翹角》 | `ootb_beginner_bookshop_signboard_01` | — | 根任務 | 無 |
| 《書鋪後庫七捆新紙有一捆總先起波紋》 | `ootb-linked-bookshop-paper-wave-001` | 《書鋪門前六塊木牌總有一塊先翹角》 | 後續／同一書鋪掌櫃與店務記錄的連續人物關係 | 非必要 |
| 《書鋪裝訂房十二冊新抄本有三冊總先鬆線》 | `ootb-linked-bookshop-binding-thread-001` | 《書鋪後庫七捆新紙有一捆總先起波紋》 | 後續／同一書鋪庫務與裝訂記錄延伸 | 非必要 |

## 關連圖
```text
《書鋪門前六塊木牌總有一塊先翹角》
  ↓ 非必要後續
《書鋪後庫七捆新紙有一捆總先起波紋》
  ↓ 非必要後續
《書鋪裝訂房十二冊新抄本有三冊總先鬆線》
```

## 共同背景基線
- 三篇都發生在江南道澄州同一間普通書鋪。
- 根任務的 `<NPC#1: 姓?-名?>` 書鋪掌櫃，在第二節點以 `<NPC#1@書鋪門前六塊木牌總有一塊先翹角: 姓?-名?>` 承接；姓名若已在前作實例化，第二節點沿用同一姓名。
- 根任務的六塊木牌、最右掛位、對街展示鏡與牆鉤問題只屬根任務事件；後作不假定任何特定根任務結局，也不令舊問題重生。
- 第二節點的七捆新紙、後庫東牆、雨槽接縫與潮氣問題只屬該節點事件；第三節點不令舊紙捆或舊雨槽問題重生。
- 第三節點的十二冊抄本、兩張壓板、木楔與收線工序是新的局部事件；其核心真相不由前兩篇 ending 決定。

## branch-specific state
- 本樹目前所有後作均無必要前置 state。
- 若角色確實跑過根任務，第二節點掌櫃只承接已發生的角色識別、姓名與既有社會記憶；不得把未取得的前作結局、報酬或資訊補成既成事實。
- 第三節點可讀取第二節點的 `bookshop_paper_moisture_resolved`、`bookshop_paper_safe_hold`、`bookshop_paper_abandoned`，但只改變店員對環境因素的初始態度與合作成本，不改第三節點真相、DC、期限或獎勵。
- 若沒有任何前作紀錄，各後作均使用自身正文的無前作紀錄基線。

## 可累積 state
- `bookshop_signboard_history_known=true/false`：只表示本桌角色是否實際經歷根任務；不改後作核心真相、DC、期限或獎勵。
- `bookshop_paper_moisture_resolved=true`：第二節點完整找出紙張起波原因並留下乾燥／移架記錄。
- `bookshop_paper_safe_hold=true`：第二節點至少隔離受潮紙並阻止其混入書會用紙。
- `bookshop_paper_abandoned=true`：第二節點未留下安全處置即退出。
- `bookshop_binding_cause_rebuilt=true`：第三節點完整重建鬆線因果並完成返工。
- `bookshop_binding_safe_delivery=true`：第三節點完成安全隔離與臨時交付。
- `bookshop_binding_misdiagnosed=true`：第三節點錯判或未留下可執行方案而失守。
- `bookshop_binding_abandoned=true`：第三節點退出且未留下隔離／返工記錄。

## 互斥 state
- `bookshop_paper_moisture_resolved`、`bookshop_paper_safe_hold`、`bookshop_paper_abandoned` 為第二節點主要結局互斥狀態。
- `bookshop_binding_cause_rebuilt`、`bookshop_binding_safe_delivery`、`bookshop_binding_misdiagnosed`、`bookshop_binding_abandoned` 為第三節點主要結局互斥狀態。
- 不同節點的 state 可累積；第二節點某一 ending 不會與第三節點某一 ending 自動互斥。

## ending／state → 後續映射
- 第二節點任一主要 ending 都不構成第三節點必要前置；有紀錄時只按第三節點正文套用態度 overlay。
- 第三節點目前沒有既存後續；其主要結局只保存自身結果，不自動解鎖未存在劇本。

## 多來源條件
目前沒有多來源節點。

## 維護註記
- 第二節點跨篇 NPC 必須保留根任務 NPC#1 的來源標記，不得另造一名同功能掌櫃取代。
- 第三節點不要求前作掌櫃存在；其委託與結算由本篇新 NPC 裝訂房管事承擔，避免前作人物狀態阻斷。
- 後作不可把任何前作 ending 升格成共同正史；若角色沒有前作紀錄，仍須可完整獨立運行。
- 前作物件、報酬與證物不因後作需要而重生；只有正文明列且實際存在的 state 可帶入。
