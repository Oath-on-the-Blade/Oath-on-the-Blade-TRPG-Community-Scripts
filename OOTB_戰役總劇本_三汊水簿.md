# OOTB 戰役總劇本：三汊水簿

## 規格頭
- `campaign_id`: `ootb-campaign-sancha-water-ledger`
- 總劇本版本：1.0.2
- 戰役狀態：已完結
- 已正式發布階段：01《低尺三分》`ootb-campaign-sancha-01-low-gauge`／`OOTB_戰役任務_三汊水簿(01)_低尺三分.md`；02《空倉十二席》`ootb-campaign-sancha-02-twelve-mats`／`OOTB_戰役任務_三汊水簿(02)_空倉十二席.md`；03《閘鏈夜響》`ootb-campaign-sancha-03-night-chain`／`OOTB_戰役任務_三汊水簿(03)_閘鏈夜響.md`；04《三汊同開》`ootb-campaign-sancha-04-three-mouths`／`OOTB_戰役任務_三汊水簿(04)_三汊同開.md`
- 規劃階段總數：4；全部已正式發布。
- 共同起點：昊國承泰二十一年，一座三水匯流的普通州城外河埠、義倉與分水閘；地名由 GM 實例化，不綁定既有固定城市。
- 主要地理：河埠水尺、州城義倉、舊分水閘、三汊堤口。
- 等級走向：6–11級；四篇依次 R7、R8、R9、R10，小型至中型。
- 共用權威：`世界知識庫/地理與世界基準/時代與世界基準.md`；其餘人物、商號、工棚均為本戰役局部設定。
- repository 總劇本只保存作者權威；每桌實際 NPC 姓名、存活、立場、state、已宣告承接結果與 `campaign_progress` 由 `campaign_save` 保存。

## 跨篇核心答案
三汊口今年春修時，承包木料的行戶以較薄閘板與回收鐵件冒充合格料，州署水工書吏為遮掩驗收疏漏，把河埠基準水尺下移三分，使帳面水位長期低於實際水位。義倉掌庫沒有參與造假，但因相信官尺，把本應墊高的十二席糧位留在低處。入夏後，閘鏈磨耗與高水位同時逼近危險線。

主要責任分三層且互不翻案：`ACTOR-CONTRACTOR` 主動以次充好；`ACTOR-CLERK` 為保職位與避賠償而移尺、改抄水簿；`ACTOR-KEEPER` 無犯案故意，但過度信任官尺而延誤搬倉。戰役開始前，上述造假、移尺、誤判已全部成立。玩家介入後，人物只依掌握資訊與利益作條件式反應。

## 跨篇真實時間線
- 春修前：承包行戶取得分水閘木鐵修繕契。
- 春修中：薄閘板與舊鏈節被混入；留下刨痕、重量差與舊鏽層。
- 驗收後：水工書吏發現數據與實測不合，把基準尺下移三分並重抄三頁水簿。
- 一月前：義倉掌庫依官尺判斷水勢尚低，沒有搬高十二席糧位。
- 七日前：閘鏈首次在無風夜裡回響；承包行戶開始回收舊料單。
- 戰役開始：兩支民間尺與官尺相差三分。
- 若玩家不介入：五日內低位義倉進水；再兩日閘鏈卡死，三汊口被迫全開或全閉，造成可避免的淹損或斷水。

## 跨篇主要行動者
### `ACTOR-CLERK`
- 身份：州署水工書吏；具體人物為 `NPC#1@戰役:三汊水簿`。
- 初始知道：官尺被自己下移、春修驗收有錯；不知道承包行戶實際換了多少料。
- 核心利益：保住職位、避免家產被追償；同時不願真的死人。
- 當前計畫：維持低報水位，私下催承包行戶補強。
- 資源／限制：能接觸水簿與差役，但無權單獨封閘；獨立實測越多越難維持說法。
- 反應：`clerk_status=exposed` 時轉向求減責並交出重抄來源；`clerk_status=active` 且玩家已公開查抄件時會試圖取走一頁副簿，但不殺人。

### `ACTOR-CONTRACTOR`
- 身份：春修承包行戶掌事；`NPC#2@戰役:三汊水簿`。
- 初始知道：自己以次充好、書吏替他遮掩；不知道義倉已受影響。
- 核心利益：保住行戶與現銀，避免被追索整批修繕款。
- 當前計畫：回收舊料單，趁夜換掉最明顯的兩節舊鏈。
- 資源／限制：有工人、車與庫棚；不控制官署。
- 反應：`contractor_evidence>=2` 時可談判退料、賠料；證據薄弱時先否認並撤工人。

### `ACTOR-KEEPER`
- 身份：義倉掌庫；`NPC#3@戰役:三汊水簿`。
- 初始知道：官尺與民尺有爭議；不知道移尺與偷料。
- 核心利益：保糧、保倉役安全、避免無證據搬倉造成擾民。
- 當前計畫：等州署正式水報。
- 反應：取得兩個獨立高水證據後立即搬高低位糧席；若被證明延誤，接受記過但不替他人背責。

### `ACTOR-WATERMEN`
- 身份：河埠量水腳戶群體，無單一戰役 NPC key。
- 利益：保住船貨與堤口安全。
- 反應：可信實測公開後協助架臨時尺、傳遞水情；玩家造謠則停止協助。

## 戰役級 NPC registry
| Key | 姓名欄 | 身份／功能 | actor_key | 首次規劃登場 | 首次正式登場 |
|---|---|---|---|---|---|
| `NPC#1@戰役:三汊水簿` | `<NPC#1@戰役:三汊水簿: 姓?-名?>` | 水工書吏 | ACTOR-CLERK | 01 | 01 |
| `NPC#2@戰役:三汊水簿` | `<NPC#2@戰役:三汊水簿: 姓?-名?>` | 承包行戶掌事 | ACTOR-CONTRACTOR | 01 | 01 |
| `NPC#3@戰役:三汊水簿` | `<NPC#3@戰役:三汊水簿: 姓?-名?>` | 義倉掌庫 | ACTOR-KEEPER | 01 | 01 |
| `NPC#4@戰役:三汊水簿` | `<NPC#4@戰役:三汊水簿: 姓?-名?>` | 分水閘老閘工 | 無 | 02 | 02 |

編號永久保留，不重用。

## campaign state
- `gauge_truth`: `unknown / suspected / proven`
- `clerk_status`: `active / cooperative / exposed / absent`
- `contractor_evidence`: 0–3
- `warehouse_moved`: `false / partial / true`
- `chain_risk`: `unknown / known / stabilized`
- `public_warning`: `none / limited / broad`
- `campaign_status`: `active / partly_completed / failed / completed`
- `campaign_progress`: 已正式結算階段數／4；提早收束時保存當時值，完整跑至末篇固定為 `4/4`。

## 階段接口
### 01《低尺三分》
- 狀態：已發布；`script_id`: `ootb-campaign-sancha-01-low-gauge`。
- 帶入：戰役初始 state；NPC #1、#2、#3。
- 為何現在：兩支民尺同日顯示官尺低三分；河埠腳戶請玩家作中立見證，州署允許旁證。
- 局部目標：判明尺差來源並決定如何處置當前水報。
- 局部真相：官尺被移低；書吏是移尺者，承包行戶與遮掩動機有關但偷料規模尚未查清。
- 輸出：`gauge_truth`、`clerk_status`、`contractor_evidence`、`public_warning`。
- endings：`SANCHA01-PROVEN`、`SANCHA01-CALIBRATED` →02、`active`；`SANCHA01-RUINED`→提早收束、`failed`。

### 02《空倉十二席》
- 狀態：已發布；`script_id`: `ootb-campaign-sancha-02-twelve-mats`。
- 解鎖：01任一 `campaign_status=active` ending；來源01。
- 帶入：01全部 state；NPC #2、#3、#4。
- 為甚麼現在：校尺後低位十二席被確認在下一次高水滲線下。
- 目標：保住糧食並查清春修材料是否影響倉渠排水。
- 局部真相：掌庫未參與造假；低位風險由錯誤水尺造成，排水木閘另用了同批薄板。
- 輸出：`warehouse_moved`、`contractor_evidence`、`chain_risk`。
- endings：`SANCHA02-CLEAR`、`SANCHA02-SAVED`→03、`active`；`SANCHA02-LOSS`→玩家可見「三汊糧損」收束、`partly_completed`。

### 03《閘鏈夜響》
- 狀態：已發布；`script_id`: `ootb-campaign-sancha-03-night-chain`。
- 解鎖：02任一 `campaign_status=active` ending；來源01+02，AND：`gauge_truth!=unknown`、`warehouse_moved!=false`。
- NPC：#1（依state）、#2、#4。
- 為甚麼現在：老閘工確認夜響來自舊鏈節偏磨，上游水位持續上升。
- 目標：查清閘鏈、阻止無記錄換鏈滅證並留下末篇安全方案。
- 局部真相：兩節舊鏈由承包行戶混入；高水下有卡死風險。
- 輸出：`chain_risk`、`contractor_evidence`、`public_warning`。
- endings：`SANCHA03-STABLE`、`SANCHA03-SAFE`→04、`active`；`SANCHA03-SCOUR`→「三汊改道」收束、`partly_completed`。

### 04《三汊同開》
- 狀態：已發布；`script_id`: `ootb-campaign-sancha-04-three-mouths`；正式檔名 `OOTB_戰役任務_三汊水簿(04)_三汊同開.md`。
- 解鎖：03任一 `campaign_status=active` ending；來源01+02+03，AND：`gauge_truth!=unknown`、`warehouse_moved!=false`、`chain_risk!=unknown`。解鎖在03正式結算時一次裁決並寫入 `campaign_save`，04開局只載入已宣告結果。
- NPC：#1–#4依 `campaign_save` 實際狀態使用正文代用品。
- 為甚麼現在：下一輪上游來水前，州署必須決定三汊閘序與春修責任處置。
- 末篇任務：以既有安全資料與責任證據建立臨時閘序、完成實際試開並處置責任封存。
- 局部真相：舊操作表沿用被移低三分的官尺基準；安全次序必須用校正尺、下游量水樁與逐級試開重建。這不改寫前三篇責任。
- 輸出：04 `ending_id`、新閘序是否建立、責任封存完整度、最終 `campaign_status`、`campaign_progress=4/4`。
- endings：`SANCHA04-SETTLED`→`completed`；`SANCHA04-SAFE`→`completed`；`SANCHA04-EMERGENCY`→末篇部分完成但原定路線已跑至末篇，`completed`並註記應急收束；`SANCHA04-BREACH`→`failed`。所有分支均正式終結本戰役，不建立自動第五階段。

## 跨篇韌性與代用品
- #1 死亡／失蹤：重抄筆序、舊副簿與尺座新孔仍可證明移尺；04另可用當日校正水報與01留底抄件，不要求其口供。
- #2 死亡／失蹤：料單重量、工棚舊料與鏈節鏽層代替供述；04安全操作由州署閘工執行，補料可由官署採買。
- #3 死亡／失蹤：義倉搬運簿、倉牆高水痕與倉役共同見證保存搬倉及回水資料。
- #4 死亡／失蹤：閘房歷年磨痕、舊尺寸木樣、值房操作圖與03卸載記錄提供鏈節及操作資料。
- 任一舊證物被毀：只讀 `campaign_save` 中仍存在的來源，不憑空重生；04安全線另由新尺、三支量水樁與逐級試開建立。責任線按現存證據降級，仍可形成 `SANCHA04-SAFE`。
- 任一地點被封：相關必要結論使用正文已存在的替代人物／記錄／現場實測；若玩家主動毀盡全部合理來源，依相應失敗或部分完成 ending 結算。

## 戰役結局邊界
戰役核心是讓三汊水工重新依真實水位安全運作，並處理已成立的責任鏈。公開追責、私下賠料或官署內部處分可有不同後果；末篇安全線完成即可讓原定四階段戰役正式走到終點，責任證據完整度決定收束品質。任何後篇不得宣稱前三篇已確認的行為其實從未發生。

完整路線跑至04後，依04正式 ending 保存 `campaign_status`、`campaign_progress=4/4`、全部既有state、主要NPC最終狀態、仍存在的證物及保管位置。01–03不可承接分支仍依各自正文提早收束，不因總綱完結而追溯改判。