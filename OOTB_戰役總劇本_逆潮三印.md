# 逆潮三印

## 戰役規格頭
- `campaign_id`: `ootb-campaign-reverse-tide-three-seals-001`
- 總劇本版本：1.1.0
- 戰役狀態：連載中；四個規劃階段均已在 `campaign_in_progress` 完成，待整體覆檢與合併 default 後正式發布／完結。
- 戰役共同起點：河洛道白沙河中游的白堤、南埠、回水倉與舊分洪閘一帶。
- 主要地理範圍：同一河運小區域；各階段提供自己的行程與整備資料。
- 預期角色等級：6–10 級；四階段不要求固定隊伍構築。
- 已正式發布階段：無；本分支尚未合併 default。
- branch 已完成待發布階段：
  - 第 1 階段 `ootb-campaign-reverse-tide-three-seals-01`／`OOTB_戰役任務_逆潮三印(01)_白堤水尺多了一道月牙刻.md`
  - 第 2 階段 `ootb-campaign-reverse-tide-three-seals-02`／`OOTB_戰役任務_逆潮三印(02)_南埠轉運單每張都多兩個針孔.md`
  - 第 3 階段 `ootb-campaign-reverse-tide-three-seals-03`／`OOTB_戰役任務_逆潮三印(03)_回水倉三張提貨票跳過同一號.md`
  - 第 4 階段 `ootb-campaign-reverse-tide-three-seals-04`／`OOTB_戰役任務_逆潮三印(04)_舊分洪閘兩把鑰匙只磨亮一把.md`
- 當前規劃階段：共 4 階段，正文已全部建立。
- repository 總劇本只保存作者權威真相、actor、NPC registry、state 與承接規則；單桌實際姓名、例外傷亡、實際物件去向與已宣告承接結果由 `campaign_save` 保存，不回寫本檔。

## 1. 跨篇核心答案
白沙河近半年出現一連串彼此看似無關的水尺誤刻、運價加價、倉票失號與舊閘維修爭議。真正根因不是單一貪污案，而是三家中型河運牙行共同建立一套「偽低水位風險—保底轉運加價—倉票延誤違約—債務收購」套利鏈。他們不能控制天候或水量，因此改動人們據以決策的記錄、貨票與風險判斷。

三家牙行透過共同帳房總理 `<NPC#1@戰役:逆潮三印: 姓?-名?>` 統一安排：先讓白堤水尺形成可被誤讀的補刻痕；再利用偽低水位消息讓三家負債船戶進入較昂貴的保底轉運；其後用錯號倉票延遲放貨製造違約；最後在舊分洪閘安全覆核中，以「事故頻仍」推動不必要的長期全面封閘，迫使負債船戶低價轉讓船、碼頭份額或倉契。

三家掌櫃都知道整體商業目的，但只有 `<NPC#1@戰役:逆潮三印>` 掌握三種現場記號與各執行者的完整對照。部分執行者只知道自己在補記、打孔、抽號或催款，不知道整套計畫；後篇不得把已成立的局部責任推翻成「其實完全無責」。

戰役名「三印」指互相校正的三種記錄痕跡：白堤補刻的月牙形定位壓痕、南埠轉運單的雙孔記號、回水倉未用票背的半月覆蠟。三者材料／工具可追到同一共用文具庫，但任何單一印記都不足以直接證明完整主謀。

舊分洪閘本身確有正常磨損：東側副閘需要半日停閘更換軸套，西側主閘仍可正常通行。套利方的問題不是「憑空捏造完全不存在的故障」，而是把有限維修誇大成十日全面封閘，再把前三篇被操弄的商業風險資料混入安全決議。

若玩家完全不介入，套利鏈會在十二日內使三戶船家接連支付高轉運費、遭遇提貨違約；第十三日舊閘以安全名義暫封，三家牙行取得債務資產並由關係修繕戶取得承包。整體只依賴地方商業資訊不對稱、記錄程序缺口與數名受僱執行者，不需要朝廷高層或超自然力量配合。

## 2. 跨篇既存時間線
- 戰役開始前 45 日：三家牙行因淡季虧損共同議價；`actor:ledger-master` 提出利用風險記錄推高短期轉運費並取得債務資產。
- 前 32 日：共用文具庫購入同批薄銅片、蠟料、打孔針；帳上記為「防潮票具」。
- 前 21 日：白堤舊水尺出現一次不影響通航的補刻試驗。
- 前 14 日：修繕戶完成舊閘例行檢查，確認東側副閘軸套偏磨，提出半日局部停閘方案。
- 前 12 日：三家牙行透過共同帳房詢問十日全面封閘承包，修繕戶要求事故資料作書面依據。
- 前 9 日：選定三家負債最重的小船戶為套利目標。
- 前 3 日：白堤水尺被正式補錯一格；第 1 階段入口形成。
- 戰役開始時：南埠已備妥雙孔空白轉運單；回水倉三個票號已被挪出正常序列。
- 無介入自然推進：第 1 日偽低水位消息擴散；第 3 日南埠加價轉運；第 7 日回水倉違約；第 12 日提出封閘安全議案。
- 玩家介入後，未來事件依 actor/state 反應產生；不得把上述日期當作無條件鐵路。

## 3. 跨篇主要行動者
### `actor:ledger-master`
- 對應 NPC：`<NPC#1@戰役:逆潮三印: 姓?-名?>`。
- 身份：三家牙行共用帳房總理，負責跨行清算。
- 初始知道：完整套利鏈、三種印具來源、各執行者工作片段。
- 不知道：玩家能力、實際保留的證據量、哪一家掌櫃會最先切割。
- 核心利益：保住共同清算權與暗佣；避免任何一家退出後把責任全推給自己。
- 當前計畫：讓三戶在封閘決議前累積足夠現金與時效違約。
- 資源：帳冊、文具庫鑰匙之一、兩名普通跑腿、熟識短途車船。
- 限制：不是武林高手，無權控制官府／門派；三家互疑後指揮能力快速下降。
- 反應：`campaign_evidence_pressure=high` 時停止新造假、保存自保帳頁；`campaign_trio_trust_broken=true` 時保留能證明三家共同授意的頁面；若被捕但對照表仍在外，可用存放點換取減責，不能改寫已成立物證。

### `actor:three-brokers`
- 身份：三家牙行掌櫃的共同決策群體；制度性 actor，不配單一 NPC key。
- 初始知道：利用水位風險、轉運加價、倉票延誤與封閘壓價的整體商業目的；不知道每次現場技術細節。
- 核心利益：取得碼頭份額與倉契，同時避免留下直接串價證據。
- 資源：三家票房、倉務往來、人手與信用網。
- 限制：三家彼此競爭，任何一方感到自己可能背鍋就會切割。
- 反應：第 1 階段若工具來源暴露，提早收走月牙尺；第 2 階段若雙孔單公開存證，停止共用口徑、各自留底；`campaign_trio_trust_broken=true` 時第 4 階段留下互相切割文書，不代表任何一家自動無罪。

### `actor:warehouse-factor`
- 對應 NPC：`<NPC#2@戰役:逆潮三印: 姓?-名?>`。
- 身份：回水倉副管事，負責票號與放貨次序。
- 初始知道：自己受命挪出三個票號並延遲指定船戶；相信只是催款手段，不知道封閘全局。
- 核心利益：保住職位並處理私人舊債。
- 資源：票柜權限、當月登記簿接觸權。
- 限制：不能改變貨物實存，也無法控制倉務值事。
- 反應：公開調查後停止繼續改號但保留舊票自保；若感到被上游倒責，可能主動找玩家。

### `actor:sluice-contractor`
- 對應 NPC：`<NPC#3@戰役:逆潮三印: 姓?-名?>`。
- 身份：舊分洪閘修繕戶。
- 初始知道：東側副閘確需有限維修；三家牙行希望封閘十日並承諾給承包；不知道前三篇造假細節。
- 核心利益：取得合理工程與長期維修權，同時避免承擔明知假資料的安全責任。
- 資源：維修人手、閘況舊記錄、工程估價、牙行往來函。
- 限制：無權單獨決定封閘；現場測試足以推翻過度方案。
- 反應：若知道事故資料可能造假，要求書面保證；若玩家取得三印對照或兩項可覆核矛盾，撤回十日方案並交出往來函自保。

## 4. 戰役級 NPC 佔位符權威列表
- `<NPC#1@戰役:逆潮三印: 姓?-名?>`：三家牙行共用帳房總理；`actor:ledger-master`；首次正式登場第 2 階段／`ootb-campaign-reverse-tide-three-seals-02`。
- `<NPC#2@戰役:逆潮三印: 姓?-名?>`：回水倉副管事；`actor:warehouse-factor`；首次正式登場第 3 階段／`ootb-campaign-reverse-tide-three-seals-03`。
- `<NPC#3@戰役:逆潮三印: 姓?-名?>`：舊分洪閘修繕戶；`actor:sluice-contractor`；首次正式登場第 4 階段／`ootb-campaign-reverse-tide-three-seals-04`。
- 三者無舊劇本 alias。編號永久保留，不因人物死亡、退出或篇章調整改派。

## 5. campaign state 權威與初始值
- `campaign_watermark_source_known`: `unknown|partial|confirmed`；初始 `unknown`；第 1 階段輸出。
- `campaign_lowwater_claim_corrected`: `false|true`；初始 `false`；第 1 階段輸出。
- `campaign_transfer_forms_preserved`: `none|partial|complete`；初始 `none`；第 2 階段輸出。
- `campaign_ledger_master_exposed`: `false|true`；初始 `false`；第 2 階段輸出。
- `campaign_trio_trust_broken`: `false|true`；初始 `false`；第 2／3 階段可輸出。
- `campaign_warehouse_sequence_proved`: `false|true`；初始 `false`；第 3 階段輸出。
- `campaign_evidence_pressure`: `low|medium|high`；初始 `low`；各篇 ending 依正式存證強度更新。
- `campaign_status`: `active|partly_completed|failed|completed`；起始 `active`，只有正式階段 ending 更新。
- `campaign_progress`: 起始 `0/4`，正式階段結算後更新為 `1/4` 至 `4/4`。
- `campaign_save` 另保存戰役 NPC 實際姓名、傷亡／被捕／合作／逃走等例外、實際保存證物、物件去向與每篇已正式裁定的下一階段解鎖路線。

## 6. 階段接口
### 第 1 階段〈白堤水尺多了一道月牙刻〉
- branch 狀態：最終稿已完成，未發布。
- `script_id`: `ootb-campaign-reverse-tide-three-seals-01`
- 檔名：`OOTB_戰役任務_逆潮三印(01)_白堤水尺多了一道月牙刻.md`
- 需要帶入 state：無；戰役起始。
- 為甚麼現在發生：巡堤人發現水尺讀數與固定泊船吃水痕矛盾，當日上午可能發出錯誤低水位公告。
- 本篇獨立目標：判明補刻原因、恢復可信讀數、留下可覆核紀錄。
- 局部真相：受僱修尺工用匿名差單附的偏位月牙銅尺補錯一格；他知道程序不合常例，但不知道套利鏈。
- 輸出：`campaign_watermark_source_known`、`campaign_lowwater_claim_corrected`、`campaign_evidence_pressure`。
- 可承接 ending：`bt01-corrected-source-confirmed`、`bt01-corrected-source-partial` → 第 2 階段，`campaign_status=active`。
- 提早收束：`bt01-local-fix-no-thread` → `partly_completed (1/4)`；`bt01-abandoned` → `failed (1/4)`。

### 第 2 階段〈南埠轉運單每張都多兩個針孔〉
- branch 狀態：最終稿已完成，未發布。
- `script_id`: `ootb-campaign-reverse-tide-three-seals-02`
- 檔名：`OOTB_戰役任務_逆潮三印(02)_南埠轉運單每張都多兩個針孔.md`
- 解鎖：第 1 階段 ending 已正式裁定可承接 AND `campaign_status=active`；再由 `campaign_watermark_source_known=confirmed|partial` OR 第 1 篇 `campaign_save` 已保存匿名差單／紙料來源之一作具體承接路線；前篇結算時固定，本篇不重算。
- 直接使用：`<NPC#1@戰役:逆潮三印>` 首次正式登場。
- 獨立目標：查明雙孔單是否有效、阻止錯誤加價、保存票具證據。
- 局部真相：票房書手按帳房總理指令先打雙孔再填指定船戶；書手不知完整套利鏈。
- 輸出：`campaign_transfer_forms_preserved`、`campaign_ledger_master_exposed`、`campaign_trio_trust_broken`、`campaign_evidence_pressure`。
- 可承接 ending：`bt02-forms-complete-master-exposed`、`bt02-forms-partial` → 第 3 階段，`campaign_status=active`。
- 提早收束：`bt02-today-only` → `partly_completed (2/4)`；`bt02-abandoned` → `failed (2/4)`。

### 第 3 階段〈回水倉三張提貨票跳過同一號〉
- branch 狀態：最終稿已完成，未發布。
- `script_id`: `ootb-campaign-reverse-tide-three-seals-03`
- 檔名：`OOTB_戰役任務_逆潮三印(03)_回水倉三張提貨票跳過同一號.md`
- 解鎖：第 2 階段 ending 已正式裁定可承接 AND `campaign_status=active` AND (`campaign_transfer_forms_preserved=partial|complete` OR `campaign_ledger_master_exposed=true`)。
- 直接使用：`<NPC#1@戰役:逆潮三印>`、`<NPC#2@戰役:逆潮三印>`。
- 獨立目標：恢復三批貨合法放貨次序、判明失號原因、處理副管事責任與即將到期違約。
- 局部真相：副管事按帳房總理要求抽出三號，並留一張半月覆蠟票自保；他不知道全局。
- 輸出：`campaign_warehouse_sequence_proved`、`campaign_trio_trust_broken`、`campaign_evidence_pressure`。
- 可承接 ending：`bt03-sequence-proved-chain-linked`、`bt03-sequence-proved-thin-link` → 第 4 階段，`campaign_status=active`。
- 提早收束：`bt03-cargo-restored-no-sluice-thread` → `partly_completed (3/4)`；`bt03-abandoned` → `failed (3/4)`。

### 第 4 階段〈舊分洪閘兩把鑰匙只磨亮一把〉
- branch 狀態：最終稿已完成，未發布。
- `script_id`: `ootb-campaign-reverse-tide-three-seals-04`
- 檔名：`OOTB_戰役任務_逆潮三印(04)_舊分洪閘兩把鑰匙只磨亮一把.md`
- 解鎖：第 3 階段 ending 已正式裁定可承接 AND `campaign_status=active` AND (`campaign_warehouse_sequence_proved=true` OR `campaign_save` 已保存由戰役 NPC 提供的舊閘往來函／口供路線)。若 `campaign_evidence_pressure=high`，開場改為搶先保存會議文書；否則為公開安全覆核。
- 直接使用：`<NPC#1@戰役:逆潮三印>`、`<NPC#2@戰役:逆潮三印>` 視前篇實際狀態；`<NPC#3@戰役:逆潮三印>` 首次正式登場。
- 為甚麼現在發生：舊閘安全覆核即將用前三篇被操弄的風險資料決定是否全面封閘。
- 獨立目標：判定真實維修需要、保存安全資料、處理套利鏈最終責任。
- 局部真相：東側副閘確需半日維修，西側主閘正常；套利方把有限維修誇成長期全面封閘，並混入前幾篇被操弄的商業風險資料。
- 完整收束：`bt04-chain-proved-safe-repair` → `completed (4/4)`。
- 部分收束：`bt04-safety-restored-chain-lost` → `partly_completed (4/4)`。
- 失敗收束：`bt04-provisional-closure`、`bt04-abandoned` → `failed (4/4)`。
- 本篇為原規劃末篇，所有 ending 均不得自動解鎖新的《逆潮三印》階段。

## 7. 跨篇反應矩陣
- `campaign_lowwater_claim_corrected=true`：第 2 階段牙行不能再聲稱白堤已確認低水位，只能說「風險未明」。
- `campaign_watermark_source_known=confirmed`：帳房總理在第 2 階段前移走剩餘月牙尺，但來不及回收已發出的雙孔單。
- `campaign_ledger_master_exposed=true`：第 3 階段副管事知道上游可能倒責；玩家展示前篇正式存證後，他直接承認抽號指令來源。
- `campaign_trio_trust_broken=true`：第 4 階段三家不再共用口徑，留下互相切割文書；不代表任何一家自動無罪。
- `campaign_evidence_pressure=high`：主要 actor 優先保存自保證據、停止新造假，而不是無限滅證；第 4 階段因此可能出現帳房自保頁或三家切割文書。
- 任何 actor 的意外死亡、被捕、倒戈或逃走由 `campaign_save` 保存；後篇使用總綱中的既存文書、其他 actor 或合法提早收束，不重新生成同一人物。

## 8. 最終收束邊界
末篇必須回答：「是否有人利用被操弄的河運風險資料取得不當商業利益」以及「哪些具體責任能被證明」。不要求玩家讓所有人定罪，也不保證地方商業制度永久改善。

完整成功至少讓舊閘決議建立在真實安全資料上，使三戶不再因虛構的長期全面封閘被迫處分資產，並以足夠來源保存商業責任鏈。`partly_completed` 必須先完整結算眼前安全／財產問題，再保留未完全釐清的責任尾巴。`failed` 必須明確保存錯誤臨時封閘或玩家退出造成的直接後果。

本戰役沒有第五階段。任何桌次一旦第 4 階段正式 ending 結算，即以該 ending 的 `campaign_status` 與 `campaign_progress=4/4` 收束；其後世界事件若另行發展，視為新的獨立內容，不自動續接本戰役。