# 逆潮三印

## 戰役規格頭
- `campaign_id`: `ootb-campaign-reverse-tide-three-seals-001`
- 總劇本版本：1.2.0
- 戰役狀態：已完結。
- 戰役共同起點：河洛道白沙河中游的白堤、南埠、回水倉與舊分洪閘一帶。
- 主要地理範圍：同一河運小區域；各階段各自提供可直接運行的行程與整備資料。
- 預期角色等級：6–10 級；共 4 階段，不要求固定隊伍構築。
- 正式階段：
  - 第 1 階段 `ootb-campaign-reverse-tide-three-seals-01`／`OOTB_戰役任務_逆潮三印(01)_白堤水尺多了一道月牙刻.md`
  - 第 2 階段 `ootb-campaign-reverse-tide-three-seals-02`／`OOTB_戰役任務_逆潮三印(02)_南埠轉運單每張都多兩個針孔.md`
  - 第 3 階段 `ootb-campaign-reverse-tide-three-seals-03`／`OOTB_戰役任務_逆潮三印(03)_回水倉三張提貨票跳過同一號.md`
  - 第 4 階段 `ootb-campaign-reverse-tide-three-seals-04`／`OOTB_戰役任務_逆潮三印(04)_舊分洪閘兩把鑰匙只磨亮一把.md`
- 本版完整內容先保存於 `campaign_in_progress`；合併 default 後，上述四階段即成為 repository 正式發布版本。若閱讀的是尚未合併的 branch，這句只描述發布時序，不改變內容完成狀態。
- repository 總劇本只保存作者權威真相、actor、NPC registry、state 與承接規則；單桌實際姓名、傷亡、物件去向與已宣告承接結果由 `campaign_save` 保存，不回寫本檔。

## 1. 跨篇核心答案
白沙河近半年出現水尺誤刻、運價加價、倉票失號與舊閘維修爭議。根因是三家中型河運牙行共同建立「偽低水位風險—保底轉運加價—倉票延誤違約—債務收購」套利鏈；他們不能控制天候或水量，因此操弄人們據以決策的記錄、貨票與風險判斷。

三家牙行透過共同帳房總理 `<NPC#1@戰役:逆潮三印: 姓?-名?>` 統一安排：白堤水尺的錯誤補刻製造風險訊號；南埠雙孔單把三家負債船戶導入較昂貴的保底轉運；回水倉抽號延遲放貨製造違約；最後把前三篇被操弄的資料混入舊分洪閘安全覆核，推動不必要的長期全面封閘，迫使三戶低價轉讓船、碼頭份額或倉契。

三家掌櫃都知道整體商業目的，但只有 `<NPC#1@戰役:逆潮三印>` 掌握三種現場記號與執行者的完整對照。部分執行者只知道自己在補記、打孔、抽號或催款，不知道全局；後篇不得推翻前篇已成立的局部責任。

「三印」是三種可互相校正的記錄痕跡：白堤月牙形定位壓痕、南埠雙孔記號、回水倉半月覆蠟。三者材料／工具可追到同一共用文具庫，但任何單一印記都不足以證明完整主謀。

舊分洪閘確有正常磨損：東側副閘需要半日停閘更換軸套，西側主閘仍可正常通行。套利方的造假不是捏造「完全無故障」，而是把有限維修誇大成十日全面封閘，再把被操弄的商業風險資料混入安全決議。

若玩家完全不介入，十二日內三戶會支付高轉運費並遭遇提貨違約；第十三日舊閘以安全名義暫封，三家牙行取得債務資產，關係修繕戶取得承包。整體只依賴地方商業資訊不對稱、記錄程序缺口與受僱執行者，不需要朝廷高層或超自然力量。

## 2. 跨篇既存時間線
- 前 45 日：三家牙行因淡季虧損共同議價；`actor:ledger-master` 提出套利鏈。
- 前 32 日：共用文具庫購入同批薄銅片、蠟料、打孔針，帳列「防潮票具」。
- 前 21 日：白堤舊水尺出現一次不影響通航的補刻試驗。
- 前 14 日：修繕戶確認東側副閘軸套偏磨，提出半日局部停閘方案。
- 前 12 日：三家牙行經共同帳房詢問十日全面封閘承包；修繕戶要求事故資料作依據。
- 前 9 日：選定三家負債最重的小船戶。
- 前 3 日：白堤水尺正式補錯一格；第 1 階段入口形成。
- 戰役開始時：南埠已備妥雙孔空白轉運單；回水倉三個票號已被挪出正常序列。
- 無介入自然推進：第 1 日偽低水位消息擴散；第 3 日南埠加價轉運；第 7 日回水倉違約；第 12 日提出封閘安全議案。
- 玩家介入後的未來事件依下列 actor/state 反應產生，不把上述日期寫成不可改變鐵路。

## 3. 跨篇主要行動者
### `actor:ledger-master`
- 對應 `<NPC#1@戰役:逆潮三印: 姓?-名?>`；三家牙行共用帳房總理。
- 知道：完整套利鏈、三種印具來源、各執行者工作片段。
- 不知道：玩家實際保存的證據量、哪一家掌櫃會先切割。
- 核心利益：保住共同清算權與暗佣，避免成為唯一替罪者。
- 資源：帳冊、文具庫鑰匙之一、兩名普通跑腿、熟識短途車船。
- 限制：不是武林高手，無權控制官府／門派；三家互疑後指揮力快速下降。
- 反應：`campaign_evidence_pressure=high` 時停止新造假並保存自保帳頁；`campaign_trio_trust_broken=true` 時保留能證明三家共同授意的頁面；若被捕，可用既存存放點換減責，不能改寫已成立物證。

### `actor:three-brokers`
- 三家牙行掌櫃共同決策群體；制度性 actor，不配單一 NPC key。
- 知道整體商業目的，不知道所有現場技術；利益是取得碼頭份額／倉契並避免留下直接串價證據。
- 資源：三家票房、倉務往來、人手與信用網；限制是三家彼此競爭。
- 反應：工具來源暴露後收走月牙尺；雙孔單公開存證後停止共用口徑；`campaign_trio_trust_broken=true` 時留下互相切割文書，不代表任何一家自動無罪。

### `actor:warehouse-factor`
- 對應 `<NPC#2@戰役:逆潮三印: 姓?-名?>`；回水倉副管事。
- 知道：自己受命挪出三個票號並延遲指定船戶；起初以為只是催款手段，不知道封閘全局。
- 核心利益：保職與處理私人舊債。
- 資源：票柜權限、登記簿接觸權；不能改變貨物實存或控制倉務值事。
- 反應：公開調查後停止繼續改號但保留舊票自保；感到被上游倒責時可能主動合作。

### `actor:sluice-contractor`
- 對應 `<NPC#3@戰役:逆潮三印: 姓?-名?>`；舊分洪閘修繕戶。
- 知道：東側確需有限維修；三家牙行希望封十日並承諾承包；不知道前三篇造假細節。
- 核心利益：取得合理工程，避免承擔明知假資料仍主張封閘的責任。
- 資源：維修人手、舊記錄、工程估價、牙行往來函；無權單獨決定封閘。
- 反應：知道事故資料可能被操弄後要求正式存證；看到可覆核矛盾後撤回十日方案並交往來函自保。

## 4. 戰役級 NPC registry
- `<NPC#1@戰役:逆潮三印: 姓?-名?>`：`actor:ledger-master`；首次正式登場第 2 階段／`ootb-campaign-reverse-tide-three-seals-02`。
- `<NPC#2@戰役:逆潮三印: 姓?-名?>`：`actor:warehouse-factor`；首次正式登場第 3 階段／`ootb-campaign-reverse-tide-three-seals-03`。
- `<NPC#3@戰役:逆潮三印: 姓?-名?>`：`actor:sluice-contractor`；首次正式登場第 4 階段／`ootb-campaign-reverse-tide-three-seals-04`。
- 三者無 legacy alias；編號永久保留，不因人物死亡、退出或篇章調整改派。

## 5. campaign state 權威
- `campaign_watermark_source_known`: `unknown|partial|confirmed`；初始 `unknown`；第 1 階段輸出。
- `campaign_lowwater_claim_corrected`: `false|true`；初始 `false`；第 1 階段輸出。
- `campaign_transfer_forms_preserved`: `none|partial|complete`；初始 `none`；第 2 階段輸出。
- `campaign_ledger_master_exposed`: `false|true`；初始 `false`；第 2 階段輸出。
- `campaign_trio_trust_broken`: `false|true`；初始 `false`；第 2／3 階段輸出。
- `campaign_warehouse_sequence_proved`: `false|true`；初始 `false`；第 3 階段輸出。
- `campaign_evidence_pressure`: `low|medium|high`；初始 `low`；各篇 ending 依正式存證更新。
- `campaign_status`: `active|partly_completed|failed|completed`；起始 `active`，只有正式 ending 更新。
- `campaign_progress`: 起始 `0/4`，正式結算後更新 `1/4` 至 `4/4`。
- `campaign_save` 另保存戰役 NPC 實際姓名、傷亡／被捕／合作／逃走等例外、實際保存證物、物件去向與已裁定承接路線。

## 6. 階段接口
### 第 1 階段〈白堤水尺多了一道月牙刻〉
- `script_id`: `ootb-campaign-reverse-tide-three-seals-01`；檔名 `OOTB_戰役任務_逆潮三印(01)_白堤水尺多了一道月牙刻.md`。
- 戰役起始，無帶入 state。巡堤人發現讀數與固定泊船吃水痕矛盾；公所委託中立江湖人判明補刻原因、恢復可信讀數、留下可覆核紀錄。
- 局部真相：受僱修尺工用匿名差單附的偏位月牙銅尺補錯一格；知道程序不合常例，不知全局。
- 跨篇接觸：月牙印具來源與匿名差單紙料。
- 輸出：`campaign_watermark_source_known`、`campaign_lowwater_claim_corrected`、`campaign_evidence_pressure`。
- 可承接：`bt01-corrected-source-confirmed`、`bt01-corrected-source-partial` → 第 2 階段，`active`。
- 提早收束：`bt01-local-fix-no-thread` → `partly_completed (1/4)`；`bt01-abandoned` → `failed (1/4)`。

### 第 2 階段〈南埠轉運單每張都多兩個針孔〉
- `script_id`: `ootb-campaign-reverse-tide-three-seals-02`；檔名 `OOTB_戰役任務_逆潮三印(02)_南埠轉運單每張都多兩個針孔.md`。
- 解鎖：第 1 ending 已正式裁定可承接 AND `campaign_status=active` AND (`campaign_watermark_source_known=confirmed|partial` OR 第 1 篇存檔已保存匿名差單／紙料來源之一)；前篇結算時固定，本篇只載入。
- 使用 `<NPC#1@戰役:逆潮三印>` 首次正式登場；三張保底轉運單即將在潮窗前生效。
- 目標：查明雙孔單是否有效、阻止錯誤加價、保存票具證據。局部真相：票房書手按帳房總理指令先打雙孔再填指定船戶；書手不知全局。
- 跨篇接觸：共用票具、帳房總理與指定船戶名單。
- 輸出：`campaign_transfer_forms_preserved`、`campaign_ledger_master_exposed`、`campaign_trio_trust_broken`、`campaign_evidence_pressure`。
- 可承接：`bt02-forms-complete-master-exposed`、`bt02-forms-partial` → 第 3 階段，`active`。
- 提早收束：`bt02-today-only` → `partly_completed (2/4)`；`bt02-abandoned` → `failed (2/4)`。

### 第 3 階段〈回水倉三張提貨票跳過同一號〉
- `script_id`: `ootb-campaign-reverse-tide-three-seals-03`；檔名 `OOTB_戰役任務_逆潮三印(03)_回水倉三張提貨票跳過同一號.md`。
- 解鎖：第 2 ending 已正式裁定可承接 AND `campaign_status=active` AND (`campaign_transfer_forms_preserved=partial|complete` OR `campaign_ledger_master_exposed=true`)。
- 使用 `<NPC#1@戰役:逆潮三印>`、`<NPC#2@戰役:逆潮三印>`；三戶到倉提貨，最早一批距違約只餘數小時。
- 目標：恢復合法放貨、判明失號原因、處理副管事責任與期限。局部真相：副管事按帳房總理要求抽出三號，留半月覆蠟票自保；不知全局。
- 跨篇接觸：覆蠟、催債函與舊閘接口。
- 輸出：`campaign_warehouse_sequence_proved`、`campaign_trio_trust_broken`、`campaign_evidence_pressure`。
- 可承接：`bt03-sequence-proved-chain-linked`、`bt03-sequence-proved-thin-link` → 第 4 階段，`active`。
- 提早收束：`bt03-cargo-restored-no-sluice-thread` → `partly_completed (3/4)`；`bt03-abandoned` → `failed (3/4)`。

### 第 4 階段〈舊分洪閘兩把鑰匙只磨亮一把〉
- `script_id`: `ootb-campaign-reverse-tide-three-seals-04`；檔名 `OOTB_戰役任務_逆潮三印(04)_舊分洪閘兩把鑰匙只磨亮一把.md`。
- 解鎖：第 3 ending 已正式裁定可承接 AND `campaign_status=active` AND (`campaign_warehouse_sequence_proved=true` OR `campaign_save` 已保存戰役 NPC 提供的舊閘往來函／口供路線)。`campaign_evidence_pressure=high` 時開場重點為保存切割／自保文書；否則為公開安全覆核。
- 使用 `<NPC#1@戰役:逆潮三印>`、`<NPC#2@戰役:逆潮三印>` 的實際狀態；`<NPC#3@戰役:逆潮三印>` 首次正式登場。
- 目標：判定真實維修需要、保存安全資料、處理套利鏈最終責任。局部真相：東側需半日維修，西側正常；套利方把有限維修誇成長期全面封閘並混入被操弄的商業風險資料。
- `bt04-chain-proved-safe-repair` → 單篇成功／`completed (4/4)`。
- `bt04-safety-restored-chain-lost` → 單篇部分成功／`completed (4/4)`；原定完整路線已跑至末篇並正式收束，故戰役層不是 `partly_completed`。
- `bt04-provisional-closure`、`bt04-abandoned` → `failed (4/4)`。
- 本篇為原規劃末篇，任何 ending 不自動解鎖新階段。

## 7. 跨篇反應矩陣
- `campaign_lowwater_claim_corrected=true`：第 2 階段不能再把白堤描述成已確認低水位，只能稱風險未明。
- `campaign_watermark_source_known=confirmed`：帳房總理提早移走剩餘月牙尺，但來不及回收已發出的雙孔單。
- `campaign_ledger_master_exposed=true`：第 3 階段副管事知道上游可能倒責；正式存證可促成其直接承認抽號來源。
- `campaign_trio_trust_broken=true`：第 4 階段三家不再共用口徑，留下切割文書；不代表任一家自動無罪。
- `campaign_evidence_pressure=high`：主要 actor 停止新造假、保存自保證據；第 4 階段可出現帳房自保頁或三家切割文書。
- actor 死亡、被捕、倒戈、逃走由 `campaign_save` 保存；後篇使用既存文書、其他 actor、替代證物或合法提早收束，不重新生成同一人物。

## 8. 跨篇關鍵依賴與回歸代用品
- `<NPC#1@戰役:逆潮三印>` 若死亡、被捕、失聯或提前合作：其功能由已保存帳頁、雙孔單來源、催債函與三家切割文書承擔；不得重生或重置。
- `<NPC#2@戰役:逆潮三印>` 若死亡／不可接觸：第 3 篇未使用票、票號序列、木模、催債函與倉務存證仍能完成局部責任；第 4 篇只讀實際保存結果。
- `<NPC#3@戰役:逆潮三印>` 若末篇死亡／逃走：兩把鑰匙、維修簿、值事啟閉試驗及已存在往來函仍能完成安全覆核；責任鏈可由前篇文件＋切割文書替代。
- 月牙尺、雙孔空白單、未使用票、往來函等若毀損：各階段正文均提供至少一組不依賴同一人／同一物的替代來源；若足以成立下一階段的接口永久失去，非末篇以正式提早戰役結局收束，不強行續開。
- 地點／機構仍存在但人員可變；後篇依可覆核記錄與職能，不假設某普通 NPC 必然在職。

## 9. 最終收束邊界
末篇回答：「是否有人利用被操弄的河運風險資料取得不當商業利益」以及「哪些具體責任能被證明」。不要求所有人定罪，也不保證地方制度永久改善。

完整成功至少讓舊閘決議建立在真實安全資料上，使三戶不再因虛構長期全面封閘被迫處分資產，並保存足夠責任來源。末篇部分成功可讓責任鏈不足，但只要眼前安全／財產問題已正式收束，因已跑到原定末篇，戰役層仍為 `completed (4/4)`。末篇失敗／放棄則 `failed (4/4)`，並保存臨時封閘或退出造成的直接後果。

本戰役沒有第五階段。第 4 階段任何正式 ending 結算後，即以該 ending 的 `campaign_status` 與 `campaign_progress=4/4` 收束；其後世界事件若另行發展，屬新的獨立內容，不自動續接本戰役。