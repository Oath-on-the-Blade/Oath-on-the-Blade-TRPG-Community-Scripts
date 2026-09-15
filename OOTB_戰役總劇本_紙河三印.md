# 紙河三印

## 戰役規格
- **campaign_id**：`campaign:paper-river-three-seals`
- **總劇本版本**：1.1.0
- **戰役狀態**：已完結
- **共同起點**：承泰二十一年，巴蜀道錦川以東青篁河紙運支線。
- **範圍**：錦川東郊紙坊帶、東溪縣庫、青篁河第三閘、上游舊竹棚與渡亭。
- **角色走向**：三階段均6–10級、R=8、中型。
- **已正式發布階段**：
  1. `ootb:campaign-paper-river:01-watermark`｜`OOTB_戰役任務_紙河三印(1)_三疊官紙少了一道水印.md`
  2. `ootb:campaign-paper-river:02-ledgers`｜`OOTB_戰役任務_紙河三印(2)_兩本閘簿同日多了一頁.md`
  3. `ootb:campaign-paper-river:03-old-seal`｜`OOTB_戰役任務_紙河三印(3)_一方舊印換了三次主人.md`
- **當前規劃下一階段**：無；末篇正式結算後不自動開第四篇。
- **世界權威**：`世界知識庫/地理與世界基準/時代與世界基準.md`、`世界知識庫/地理與世界基準/昊國地理.md`；東溪縣、青篁河紙坊與本戰役人物均為局部真相。
- **桌次分工**：本檔定義作者權威；實際姓名、ending、例外、解鎖裁定由 `campaign_save` 保存，不寫回 repository。

## 跨篇核心答案
前任庫吏病故後，一方未銷毀的舊驗紙印流入舊貨市。紙貨中介 `<NPC#1@戰役:紙河三印: 姓?-名?>` 發現地方初驗仍把舊式印痕當作官紙可信憑據，於是用它加工空白紙，分批賣給需要掩飾貨單、欠稅與轉運來源的人。河閘書手 `<NPC#2@戰役:紙河三印: 姓?-名?>` 因家債替中介改寫船次頁碼；竹料掌櫃 `<NPC#3@戰役:紙河三印: 姓?-名?>` 只知高價收竹，不知官紙用途；縣庫主簿 `<NPC#4@戰役:紙河三印: 姓?-名?>` 察覺庫存異常卻先誤判紙坊偷料。

舊印只是工具。持續危害來自「只看表面印痕」的初驗漏洞。只抓中介、書手或收回舊印，都不能自動證明流程已修補。若玩家不介入，第3日封坊、第4日舊印轉手、第5日書手逃離，河運與紙價一併受阻。

## 跨篇時間線
半年前前任庫吏病故、舊印散入舊貨；五個月前中介買印並試印；四個月前拉攏書手改頁；三個月前高價分散收竹；近月三批官紙序列與庫簿不符；第一篇開始時主簿準備封坊。後續轉印、催逃與封存均由玩家是否暴露中介、是否保全帳線等 state 條件觸發，並非固定劇情。

## 主要行動者
### `actor_broker`｜`NPC#1@戰役:紙河三印`
紙貨中介。知道舊印可騙初驗、書手改頁範圍與部分買家暗記；不知道主簿已逐疊核對。核心利益是維持收入並減輕刑責。正常時小批出貨；`broker_exposed=true` 時先轉印後滅帳；`old_seal_status=secured/destroyed` 時改以 `buyer_marks=partial` 求減責。資源是船腳、舊貨與紙貨人脈，限制是無官權、買家彼此隔離。

### `actor_scribe`｜`NPC#2@戰役:紙河三印`
第三閘書手。知道自己三次改頁、交接暗記與舊竹棚；不知道舊印來源及買家。核心利益是保家人與工作。獲安全作證則合作；被公開指認且無保護則逃走，但草頁仍留作替代證據。

### `actor_bamboo`｜`NPC#3@戰役:紙河三印`
竹料掌櫃。知道高價收竹者、日期與貨棧；誤以為同行囤貨。要保商譽與訂金。證明官紙用途後願交相關帳，但要求收據。

### `actor_clerk`｜`NPC#4@戰役:紙河三印`
東溪縣庫主簿。知道庫存與水印序列不符；初始誤判紙坊。核心利益是恢復庫務可信度。兩條獨立證據指向造紙後加工時暫緩封坊；末篇有權發布縣庫臨時驗收令，但永久改制仍須上報。

## 戰役級 NPC registry
| Key | 姓名欄 | 身份 | actor_key | 首次正式登場 |
|---|---|---|---|---|
| `NPC#1@戰役:紙河三印` | 姓?-名? | 紙貨中介 | `actor_broker` | 第一階段 `ootb:campaign-paper-river:01-watermark` |
| `NPC#2@戰役:紙河三印` | 姓?-名? | 第三閘書手 | `actor_scribe` | 第二階段 `ootb:campaign-paper-river:02-ledgers` |
| `NPC#3@戰役:紙河三印` | 姓?-名? | 竹料掌櫃 | `actor_bamboo` | 第一階段 |
| `NPC#4@戰役:紙河三印` | 姓?-名? | 縣庫主簿 | `actor_clerk` | 第一階段 |

## Campaign state
- `watermark_chain`: `unknown/partial/proven`
- `ledger_chain`: `unknown/partial/proven`
- `broker_exposed`: bool
- `scribe_status`: `at_post/protected/fled/detained`
- `old_seal_status`: `with_broker/moved/secured/destroyed`
- `paper_mills_status`: `open/restricted/sealed`
- `buyer_marks`: `none/partial/recovered`

## 第一階段接口：三疊官紙少了一道水印
- **輸入**：共同起點。
- **局部真相**：紙坊沒有偷料；異常紙由舊印加工後混入。
- **任務目標**：判斷缺印來源並向主簿交付可核驗結論。
- **輸出**：`watermark_chain`、`paper_mills_status`、可能 `broker_exposed`。
- `ending_stage1_proven`：`active`；第二篇解鎖。`watermark_chain=proven`。
- `ending_stage1_partial`：`active`；第二篇解鎖，改以全面核簿開場。`watermark_chain=partial`。
- `ending_stage1_wrong`：完成結局但不可承接；`partly_completed (1/3)`，紙坊被封，玩家沒有河運接口，原定第二篇不發生。
- `ending_stage1_abandon`：`failed (1/3)`，中斷戰役。
- **解鎖裁定時點**：第一篇正式結算時一次寫入 `campaign_save`；第二篇開局不重算。

## 第二階段接口：兩本閘簿同日多了一頁
- **解鎖**：`ending_stage1_proven OR ending_stage1_partial`；前篇已裁定。
- **較早 state 影響**：`watermark_chain` 決定玩家是否已有指定日期；`broker_exposed` 決定危機起始格。
- **局部真相**：書手因家債改頁以遮蔽三批紙貨船次，沒有參與加工。
- **目標**：保全帳線、查明改頁目的。
- `ending_stage2_trace`：`active`，`ledger_chain=proven`，第三篇解鎖。
- `ending_stage2_burned`：`active`，`ledger_chain=partial`，仍取得舊竹棚接口，第三篇解鎖。
- `ending_stage2_closed`：完成結局但不可承接；`partly_completed (2/3)`，玩家把書手當完整答案，沒有舊印接口。
- `ending_stage2_abandon`：`failed (2/3)`。
- **解鎖裁定**：第二篇結算時一次寫入；第三篇不重算。

## 第三階段接口：一方舊印換了三次主人
- **解鎖**：`ending_stage2_trace OR ending_stage2_burned`，且該次結算已裁定第三篇解鎖。
- **累積來源**：第一篇 `watermark_chain` 決定流程證據完整度；第二篇 `scribe_status` 決定是否有人辨暗記；`old_seal_status` 決定追索地點；任何 NPC 缺席都有草頁、回條、試紙或收據替代。
- **局部真相**：舊印只是工具；真正持續問題是單一印痕初驗。
- **目標**：處理舊印實體狀態、制度漏洞與責任交付。
- `ending_stage3_reformed`：印與流程均處理，`completed (3/3)`。
- `ending_stage3_seal_only`：只處理舊印，核心追索正式結算，流程風險作世界後果保存，`completed (3/3)`。
- `ending_stage3_lost`：舊印外流但制度停用舊印痕，`completed (3/3)`。
- `ending_stage3_abandon`：`failed (3/3)`。

## 提早戰役收束
### `ending_stage1_wrong`｜封住了錯的門
已回答眼前「庫存如何處理」，未回答河運加工來源；`paper_mills_status=sealed`。主簿、紙坊依第一篇實際狀態保存。下一篇不發生，因玩家沒有可追河運接口。玩家可見收束先交代封坊與停工，再以夜色中仍有一船空紙過閘作不劇透尾巴。

### `ending_stage2_closed`｜帳清，人未清
已回答重頁責任，未回答舊印去向；`scribe_status=detained`、`ledger_chain=partial`。第三篇不發生，因本次結算沒有舊竹棚／轉印接口。玩家可見收束先交代書手被帶走與帳案結束，再以縣庫仍找不到缺號空紙作尾巴。

## 跨篇依賴與例外回歸
- **書手失聯／死亡**：草頁＋船夫回條＋重穿痕跡可替代其口供；第三篇暗記可由繩結實物替代。
- **帳簿毀損**：縣庫收貨簿、草頁與船夫回條可重建 `ledger_chain=partial`。
- **中介被捕／逃走／提前合作**：舊印追索由試紙、舊貨收據與交接地點繼續；人物本人不是末篇必要單點。
- **舊印毀損／外流**：末篇仍可用碎片、試紙、見證或收據確定狀態，並以流程修補切斷本地漏洞。
- **主簿失能或失去職權**：若此例外由玩家／世界在前篇造成，`campaign_save` 必須保存；縣庫當值代理人可依法接手既有封存與臨時驗收程序，但不能改寫前篇已裁定的 ending。若連縣庫職能本身也不可用，末篇以「證據交付但制度令無法生效」形成 `derived` 結局，不虛構新權限。

## 最終收束邊界
末篇必須結算舊印實體狀態、地方初驗漏洞是否停用、紙坊／書手／中介責任如何區分。買家暗記可以部分遺失，不要求抓盡所有買家；戰役核心在於確認誰建立並利用漏洞、漏洞如何運作，以及玩家最終使其停止或留下甚麼明確風險。