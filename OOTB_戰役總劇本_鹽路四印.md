# OOTB 戰役總劇本：鹽路四印

## 規格頭
- `campaign_id`: `ootb_campaign_saltroad_four_seals`
- 總劇本版本：1.1
- 戰役狀態：已完結
- 已正式完成階段：
  1. `ootb_campaign_saltroad_four_seals_01_baidi_misprint`｜`OOTB_戰役任務_鹽路四印(1)_白堤錯印.md`
  2. `ootb_campaign_saltroad_four_seals_02_shimen_night_seal`｜`OOTB_戰役任務_鹽路四印(2)_石門夜封.md`
  3. `ootb_campaign_saltroad_four_seals_03_luwan_empty_ticket`｜`OOTB_戰役任務_鹽路四印(3)_鷺灣空票.md`
  4. `ootb_campaign_saltroad_four_seals_04_four_seals_one_account`｜`OOTB_戰役任務_鹽路四印(4)_四印同帳.md`
- 當前規劃：四階段全部完成；沒有第五階段。
- 共同起點：承泰二十一年，江南道北部一條連接鹽倉、河埠、官道驛站與鹽場的地方鹽運支線。
- 主要地理：白堤鎮、青螺埠、石門驛、鷺灣鹽場；均為江南道局部新增地點，不改寫共用正典。
- 等級走向：6–9 → 7–10 → 8–11 → 9–12。
- 共用權威：Handbook `世界知識庫/`、`遊玩規則/`、`內容庫/`；單桌實際姓名、死亡、物件持有、例外狀態與已宣告承接結果只進 `campaign_save`。

## 跨篇核心答案
地方原有「先移實物、後補正票」的救急挪倉慣例，用來避免洪水、封航或倉容不足令官鹽受潮。白堤鹽課副吏 `actor_deputy_clerk` 發現這套慣例會產生短暫時間差，逐步把它改造成收取加急費的套利制度：河埠牙人 `actor_wharf_factor` 提前換船牌，石門驛驛丞 `actor_relay_keeper` 只替急調文書補日期，鷺灣鹽場仍按舊例先記實際移倉再補正票。倉印、船牌、驛封、場票分處四地，使各單位只能看見一段。

責任邊界固定如下：副吏設計並主要受益；牙人明知提前換牌並收分成；驛丞違規重封但不知道完整套利額；鷺灣書吏沿用救急舊例且沒有參與抽成。兩家地方鹽商知道可付加急費換優先出貨，不知道完整四印結構。守規矩的鹽戶、倉役與被追補的小吏承受主要損害。

戰役開始前已成立：救急舊例、雙帳時間差、四印分離、核心人物的既有合作、兩家鹽商曾付費、至少四次成功套利。玩家介入後才可能發生的滅證、合作、公開搜捕、證物毀損、拘押與交易，只按各階段 ending／state 或單桌例外資料成立。

## 跨篇真實時間線
1. 三年前：洪水季形成救急挪倉慣例。
2. 兩年前：副吏開始挑選時間差批次收加急費。
3. 一年前：牙人加入換牌；驛丞因修繕欠款開始替部分急件補期重封。
4. 近半年：套利頻率上升，四類憑證出現可交叉比對的矛盾，倉役與鹽戶開始被追補。
5. 戰役開始：巡核吏取得三張日期互撞倉票，準備先查白堤。
6. 玩家不介入：巡核吏先追查腳戶；副吏切割牙人並轉移私簿；牙人自保；驛丞停止合作；地方最後傾向停用整套救急慣例，套利責任仍不完整。

## 跨篇主要行動者
### `actor_deputy_clerk`
- 戰役 NPC：`<NPC#1@戰役:鹽路四印: 姓?-名?>`
- 身份：白堤鹽課副吏。
- 初始認知：知道完整雙帳結構、四印用途、牙人與驛丞角色；不知道巡核吏最初掌握哪些票。
- 核心利益：保住職位與地方信用、償清私人債務、維持調鹽控制力。
- 資源：鹽課文書權限、私簿、兩名普通書手、地方跑腿。
- 限制：不能合法改動已封存月結冊，沒有公開調兵權。
- 初始計畫：把矛盾解釋成舊例疏漏，必要時讓倉役或牙人承擔責任。
- 反應：`campaign_evidence_link>=2` 時轉移私簿；`deputy_exposed=true` 時優先交易；`factor_cooperates=true` 時停止否認分成，改爭論責任範圍。

### `actor_wharf_factor`
- 戰役 NPC：`<NPC#2@戰役:鹽路四印: 姓?-名?>`
- 身份：青螺埠牙人。
- 初始認知：知道哪些批次先走後補、自己收過分成；不知道驛封操作與鹽場完整資料。
- 核心利益：保住生意與船戶信任，不替副吏扛全部責任。
- 資源：船戶消息、舊船牌、貨棚與牙行收支。
- 限制：沒有官面保護。
- 反應：無證公開指控時散播封埠恐慌；證明副吏準備棄他時可 `factor_cooperates=true` 並交出對牌／分成資料。

### `actor_relay_keeper`
- 戰役 NPC：`<NPC#3@戰役:鹽路四印: 姓?-名?>`
- 身份：石門驛驛丞。
- 初始認知：知道自己替六批急調文書重封，以為只是補正運期，不知道完整套利額。
- 核心利益：補回驛站修繕欠款、避免驛卒替自己受罰。
- 資源：夜班簿、舊封模、驛卒排班。
- 限制：不能控制鹽場或河埠資料。
- 反應：責任被區分時願交封模；遭公開羞辱、威脅或強奪官封時先藏模並上報。

### `actor_inspector`
- 戰役 NPC：`<NPC#4@戰役:鹽路四印: 姓?-名?>`
- 身份：奉命覆核地方鹽課帳目的巡核吏。
- 初始認知：知道三張倉票日期矛盾，起初誤判主因為腳戶偷鹽。
- 核心利益：迅速止損並取得可交付證據鏈，避免無證大捕與全面停運。
- 資源：查簿、封存文書及要求地方官差協助的正式權限。
- 限制：沒有成鏈證據時不願定完整責任。
- 反應：`campaign_evidence_link>=3` 時轉查制度鏈；單一口供永遠不足以完成最終責任鏈。

## 戰役級 NPC registry
| Key | 姓名欄 | 身份 | actor_key | 首次規劃登場 | 首次正式登場 |
|---|---|---|---|---|---|
| `NPC#1@戰役:鹽路四印` | 姓?-名? | 白堤鹽課副吏 | `actor_deputy_clerk` | 1 | 階段1／`ootb_campaign_saltroad_four_seals_01_baidi_misprint` |
| `NPC#2@戰役:鹽路四印` | 姓?-名? | 青螺埠牙人 | `actor_wharf_factor` | 1 | 階段1／`ootb_campaign_saltroad_four_seals_01_baidi_misprint` |
| `NPC#3@戰役:鹽路四印` | 姓?-名? | 石門驛驛丞 | `actor_relay_keeper` | 2 | 階段2／`ootb_campaign_saltroad_four_seals_02_shimen_night_seal` |
| `NPC#4@戰役:鹽路四印` | 姓?-名? | 巡核吏 | `actor_inspector` | 1 | 階段1／`ootb_campaign_saltroad_four_seals_01_baidi_misprint` |

編號永久保留，不因死亡、退出或篇章改動重用。

## Campaign state registry
- `campaign_evidence_link`: 0–4；由各階段正式 ending 增加，表示已可靠連起的獨立憑證類型數。
- `deputy_exposed`: boolean；副吏身份是否已被可靠歸因；第三階段 `ledger_and_method` 可確立，其他衍生結局按實際證據保存。
- `factor_cooperates`: boolean；牙人是否自願提供對牌／分成資料；第一階段可建立，後篇只讀取，不強迫重置。
- `relay_truth_known`: boolean；第二階段 ending 建立，表示已確認驛封是受要求重封而非單純偽造。
- `relay_seal_secured`: boolean；第二階段 ending 建立，表示舊封模是否安全封存。
- `saltfield_ledger_secured`: boolean；第三階段 ending 建立，表示鷺灣原始底簿是否安全。
- `public_sweep`: boolean；第一階段 `sweep_and_scatter` 或相應衍生結局可建立；若該桌仍因例外進入後篇，後篇只能使用官面／已封存資料。
- `campaign_status`: `active | partly_completed | failed | completed`；每篇 ending 正式寫入。
- `campaign_progress`: 已正式結算階段數／4。
- NPC 死亡、失蹤、拘押、傷勢、實例姓名與其他未列成固定跨篇 state 的例外，依 `campaign_save` 保存，不在 repository 總綱預先虛構。

## 階段一接口：《白堤錯印》
- 狀態：已完成；`ootb_campaign_saltroad_four_seals_01_baidi_misprint`。
- 建議等級：6–9。
- 輸入：共同基線；無前置。
- 使用 NPC：#1、#2、#4。
- 為何現在：巡核吏取得三張日期互撞倉票。
- 玩家介入：先做小範圍核對，避免立即封鎮。
- 單篇目標：查明錯票直接成因並處理倉役追補危機。
- 局部真相：副吏命先放後補，牙人提前換牌；普通倉役不知道套利。
- 跨篇接觸：首次把倉印與船牌證明為同批貨。
- 輸出：`campaign_evidence_link`、`factor_cooperates`、`public_sweep` 及單桌例外。
- `seal_chain_proved`：`campaign_evidence_link=1`；可承接階段2；`active 1/4`。
- `local_fault_settled`：提早 `partly_completed 1/4`；《錯印止於白堤》；階段2鎖定。
- `sweep_and_scatter`：提早 `failed 1/4`；《封倉之後》；階段2鎖定。
- `abandon`：提早 `failed 1/4`。

## 階段二接口：《石門夜封》
- 狀態：已完成；`ootb_campaign_saltroad_four_seals_02_shimen_night_seal`。
- 建議等級：7–10。
- 完整解鎖：階段1 `seal_chain_proved` AND `campaign_evidence_link>=1`，並由階段1結算時凍結承接結果。
- 使用 NPC：#2、#3、#4；#1 按 state 遠端反應。
- 為何現在：船牌顯示同批貨在實際過驛後才取得封條日期。
- 玩家介入：在正式封存驛站前查清夜班重封來源。
- 單篇目標：查明六次重封責任與目的，保住夜班資料。
- 局部真相：驛丞違規重封但只知道補期，副吏刻意不讓他看完整差額。
- 輸出：`relay_truth_known`、`relay_seal_secured`、`campaign_evidence_link`。
- `night_seal_secured`：`campaign_evidence_link=2`；可承接階段3；`active 2/4`。
- `truth_without_seal`：若 `factor_cooperates=true OR campaign_evidence_link>=2`，可承接階段3並為 `active 2/4`；否則提早 `partly_completed 2/4`，《夜簿留字》。
- `relay_broken`：提早 `failed 2/4`。
- `abandon`：提早 `failed 2/4`。

## 階段三接口：《鷺灣空票》
- 狀態：已完成；`ootb_campaign_saltroad_four_seals_03_luwan_empty_ticket`。
- 建議等級：8–11。
- 完整解鎖路線 A：階段2 `night_seal_secured` AND `campaign_evidence_link>=2`。
- 完整解鎖路線 B：階段2 `truth_without_seal` AND (`factor_cooperates=true` OR `campaign_evidence_link>=2`)。
- 承接判定由階段2正式結算時凍結；本篇開局不重算。
- 使用 NPC：#1、#2、#4；#3 只讀已保存資料。
- 為何現在：前三印日期鏈指向鷺灣「已出票但未同日出場」的原始底票。
- 玩家介入：在副吏轉移私簿前保住底簿並釐清鹽戶責任。
- 單篇目標：保住底簿、證明場票如何被利用，避免把救急舊例本身誤判為整體犯罪。
- 局部真相：鹽場書吏沿用舊例且未參與抽成；副吏利用時間差套利。
- 輸出：`saltfield_ledger_secured`、`campaign_evidence_link`、`deputy_exposed`。
- `ledger_and_method`：`campaign_evidence_link=3`、`saltfield_ledger_secured=true`；可承接階段4；`active 3/4`。
- `method_only`：若 `campaign_evidence_link>=3` 可承接階段4並為 `active 3/4`；否則提早 `partly_completed 3/4`，《鹽場無罪》。
- `wrong_culprit`：提早 `partly_completed 3/4`，《一冊帳的盡頭》；階段4鎖定。
- `abandon`：提早 `failed 3/4`。

## 階段四接口：《四印同帳》
- 狀態：已完成；末篇；`ootb_campaign_saltroad_four_seals_04_four_seals_one_account`。
- 建議等級：9–12。
- 完整解鎖路線 A：階段3 `ledger_and_method` AND `campaign_evidence_link>=3`。
- 完整解鎖路線 B：階段3 `method_only` AND `campaign_evidence_link>=3`。
- 承接判定由階段3正式結算時凍結；本篇開局只載入結果。
- 使用 NPC：#1、#2、#4；#3 只按存檔作證或缺席。
- 為何現在：至少三印已連成制度鏈，副吏知道調查逼近私簿與收款。
- 玩家介入：在私簿轉移與責任切割完成前建立可交付責任鏈。
- 單篇目標：處理副吏、私簿、牙人分成與救急慣例的制度後果。
- 局部真相：副吏是套利制度設計與主要受益者；牙人明知參與；驛丞責任較窄；鷺灣書吏不知抽成。
- `four_seals_proved`：完整責任鏈成立並保留救急機制；`completed 4/4`。
- `culprit_without_reform`：責任成立但地方全面停用救急慣例；`completed 4/4`。
- `bargained_account`：副吏交簿、返還並接受正式處分，其他來源完成互證；`completed 4/4`。
- `proof_collapses`：末篇證據不足以完成責任鏈；`failed 4/4`；前三篇已成立事實不回滾。
- `abandon`：`failed 4/4`。

## 跨篇關鍵依賴與例外回歸
- 倉票、船牌、驛封模、場票底簿與私簿均不是唯一單點；各階段正文提供具體替代資料。任何單件遺失只按該篇 ending／已凍結承接結果影響後續。
- NPC#2 死亡／失蹤：船戶記錄、河埠秤簿、掛鉤痕跡與牙行收支替代；不生成死後口供。
- NPC#3 死亡／失蹤：夜班簿、封模與驛卒證詞替代；若相關來源均失去，由階段2 ending 正式決定是否仍可承接。
- NPC#1 提前被捕：後篇在看管狀態下核對私簿與收款，不安排逃亡；被捕不等於責任鏈成立。
- NPC#1 死亡／失蹤：末篇以兩家鹽商付款、牙人分成／牙行收支、月結差額與前三印資料互證。
- 私簿毀損：末篇使用鹽商付款、牙人分成／牙行收支與月結差額三方互證。
- `relay_seal_secured=false`：後篇不得重生封模，改讀夜班簿、里程與驛馬資料。
- `saltfield_ledger_secured=false`：後篇不得重生原簿，改讀騎縫副本或鹽戶小票＋秤臺日簿。
- 任何固定人物、物件或地點因單桌前史出現額外狀態，由 `campaign_save` 保存；後篇只使用功能等價且正文已存在的制度資料／替代來源，或按既有 ending 提早收束。

## 最終收束原則
戰役完成判準是能可靠區分四印制度中的責任：誰設計並收費、誰明知參與、誰只違規補正、誰只是沿用救急慣例。末篇不得以「抓到一個人」或單一自白代替證據鏈。所有提早收束與末篇失敗均保存已成立的洗清、責任、人物與物件後果，不因戰役停止而回滾。