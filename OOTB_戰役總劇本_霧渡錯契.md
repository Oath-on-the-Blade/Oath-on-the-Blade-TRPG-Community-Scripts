# 霧渡錯契

## 戰役規格
- `campaign_id`: `ootb_campaign_mist_ferry_false_contract_20260831`
- 總劇本版本：1.1.0
- 戰役狀態：已完結
- 已正式發布的階段劇本：
  1. `ootb_campaign_mist_ferry_01_half_contract_20260831`｜`OOTB_戰役任務_霧渡錯契(1)_雨夜半契.md`
  2. `ootb_campaign_mist_ferry_02_archive_seal_20260831`｜`OOTB_戰役任務_霧渡錯契(2)_舊庫無名印.md`
  3. `ootb_campaign_mist_ferry_03_empty_boats_20260831`｜`OOTB_戰役任務_霧渡錯契(3)_兩艘空船.md`
  4. `ootb_campaign_mist_ferry_04_ferry_rights_20260902`｜`OOTB_戰役任務_霧渡錯契(4)_重分渡權.md`
- 當前規劃中的下一階段：無；戰役於第4階段正式收束。
- 共同起點：劍南道一處普通河谷渡鎮與上下游村落；不建立固定世界地標。
- 預期等級走向：3–5級；R4；每篇3–5 PC；小型至中型。
- 共用世界基準：Handbook 世界知識庫之時代／地理基準；本戰役渡鎮、人物與渡權均為局部劇本事實。
- repository 總劇本與單桌 `campaign_save` 分離；實際姓名、死亡、失蹤、物品毀損及已宣告承接結果只由 GM 存檔保存。

## 跨篇核心答案（GM／作者）
渡鎮近半年出現一批仿舊渡契。退役書手為錢仿製六份；河運牙人買入並分散使用，以低價契壓低村戶渡資；地方胥吏故意讓廢止印樣規格外流，並放過一份明顯異常契，使真假契混雜足以推動舊案重查。胥吏的真正利益是追回家族十多年前失去的舊碼頭份額：待爭議擴大後先暫收渡權，再讓遠房姻親代理參與重分。

三人不是完整同盟。書手只知道牙人買貨；牙人知道官面有人曾放行異常舊契，但不知道家族奪權目的；胥吏知道牙人在利用假契，卻保留可否認距離。後篇不得洗白書手與牙人，也不得把胥吏改寫成遙控第一篇所有行動的全知黑手。

核心因果：印樣外流 → 書手仿契 → 牙人散用與壓價 → 真偽契混雜 → 胥吏推動重查／暫收 → 代理提前投件 → 若無阻止則重分渡權。

戰役開始時已成立：印樣外流、六份假契製成、至少三份使用、胥吏家族舊份額利益。尚未固定：殺人、焚冊、暴力奪權等事件；只按 actor 在玩家介入後的風險認知反應。

## 跨篇真實時間線
- 十多年前：胥吏家族失去一處舊碼頭份額。
- 六個月前：`actor_clerk` 抄存廢止渡契印樣規格。
- 四個月前：`actor_broker` 經中間人委託 `actor_scribe` 仿舊契。
- 三個月前：首批假契投入使用並壓低渡資。
- 一個月前：`actor_clerk` 故意放過一份異常舊契。
- 一週前：真假契同時流通，老船戶提出異議。
- 第1階段：雨夜半契公開引爆爭議。
- 第2階段：追查舊庫印樣接觸鏈。
- 第3階段：牙人因風險回收／毀棄假契與交易記錄。
- 第4階段：若前三篇意圖鏈成立，胥吏提前推動暫收與重分，代理申請在公告前送入。
- 若玩家完全不介入：書手離鎮、牙人繼續散契、舊庫封存、三渡暫收，代理人進入重分序位。

## 跨篇主要行動者
### `actor_scribe`｜退役書手
- 戰役 NPC：`<NPC#1@戰役:霧渡錯契: 姓?-名?>`
- 知道：自己仿六份契、牙人是買家、紙與印樣規格由中間供應鏈而來。
- 不知道：胥吏家族目的。
- 利益：拿尾款、保家人、避免成為唯一主謀。
- 資源／限制：仿舊筆法、樣紙、熟識腳夫；不擅武、不願殺人。
- 反應：暴露且自由時先藏樣紙、準備離鎮；獲保全承諾並見牙人利用證據時可合作。

### `actor_broker`｜河運牙人
- 戰役 NPC：`<NPC#2@戰役:霧渡錯契: 姓?-名?>`
- 知道：書手來源、官面曾放過異常契。
- 不知道：胥吏家族重分目的。
- 利益：壓渡資、保牙行、避免官責。
- 資源／限制：現銀、腳夫、真假契、租船；依賴商譽，不願公開暴力。
- 反應：網路暴露後回收假契、嫁禍書手；證據被保全後傾向談判。

### `actor_clerk`｜地方胥吏
- 戰役 NPC：`<NPC#3@戰役:霧渡錯契: 姓?-名?>`
- 知道：印樣外流、牙人用假契、家族舊份額、代理安排。
- 利益：令現有渡權顯得混亂，促成暫收與重分，同時維持表面清白。
- 資源／限制：舊庫接觸權、初驗程序、人情；不能公開改寫已登記日期，直接提供印樣若被證明風險極高。
- 反應：`seal_source_known=true` 時先封庫；第3階段意圖鏈逼近時提前推動暫收；代理提前投件曝光後轉為程序拖延。

### `actor_boatfolk`｜受影響船戶群體
- 抽象 actor，無 NPC key。
- 利益：保住合法渡運收入與通行秩序。
- 反應：爭議惡化時停夜渡；證據鏈清楚時願作證並維持臨時輪渡。

## 戰役級 NPC registry
1. `<NPC#1@戰役:霧渡錯契: 姓?-名?>`：退役書手；`actor_scribe`；首次正式登場第1階段。
2. `<NPC#2@戰役:霧渡錯契: 姓?-名?>`：河運牙人；`actor_broker`；首次正式登場第1階段。
3. `<NPC#3@戰役:霧渡錯契: 姓?-名?>`：地方胥吏；`actor_clerk`；首次正式登場第2階段。
4. `<NPC#4@戰役:霧渡錯契: 姓?-名?>`：老船戶代表；屬 `actor_boatfolk` 的具體跨篇人物；首次正式登場第1階段。
5. `<NPC#5@戰役:霧渡錯契: 姓?-名?>`：舊庫看守；首次正式登場第2階段；提供保管流程與接觸紀錄，不預設涉案。
- 上述編號永久保留；任何桌次實際姓名與例外狀態由 `campaign_save` 保存。

## Campaign state
- `half_contract_secured`: `none / one_half / both_halves`
- `scribe_exposed`: `false / true`
- `scribe_status`: `free / cooperative / detained / fled / dead_or_unavailable`
- `broker_network_exposed`: `false / true`
- `broker_status`: `active / cooperative / detained / fled / unavailable`
- `seal_source_known`: `false / true`
- `clerk_intent_proven`: `false / true`
- `old_archive_status`: `open / supervised / sealed / damaged`
- `boatfolk_trust`: `low / neutral / high`
- `campaign_status`: `active / partly_completed / failed / completed`
- `campaign_progress`: 已正式結算階段數/4。

## 階段接口
### 第1階段《雨夜半契》｜已發布
- `script_id`: `ootb_campaign_mist_ferry_01_half_contract_20260831`
- 輸入：第一階段，無前篇 state。
- NPC：#1、#2、#4。
- 局部真相：兩半來自同一份假契；持契雙方均非偽造者。
- 輸出：`half_contract_secured`、`scribe_exposed`、`boatfolk_trust`。
- `E1_CHAIN_FOUND`：至少一半契＋書手線索 → 可承接第2階段，`active`。
- `E1_ORDER_ONLY`：止衝突但證物與書手線索全失 → 提早 `partly_completed (1/4)`。
- `E1_ABANDON`：放棄 → `failed`。

### 第2階段《舊庫無名印》｜已發布
- `script_id`: `ootb_campaign_mist_ferry_02_archive_seal_20260831`
- 解鎖：第1 `E1_CHAIN_FOUND` AND `scribe_exposed=true`。
- NPC：#3、#4、#5；#1依 state。
- 局部真相：看守失職但非主謀；胥吏曾抄存印樣。
- 輸出：`seal_source_known`、`old_archive_status`、`clerk_intent_proven` 初步狀態。
- `E2_SOURCE_PROVEN`：印樣接觸鏈指向胥吏 → 可承接第3階段，`active`。
- `E2_LEAK_ONLY`：只證明制度漏洞 → 提早 `partly_completed (2/4)`。
- `E2_ABANDON`：放棄 → `failed`。

### 第3階段《兩艘空船》｜已發布
- `script_id`: `ootb_campaign_mist_ferry_03_empty_boats_20260831`
- 解鎖：第1 `scribe_exposed=true` AND 第2 `seal_source_known=true` AND (`scribe_status=cooperative` OR `half_contract_secured!=none` OR 第2階段已有印樣比對記錄)。
- NPC：#2、#4；#1/#3依 state。
- 局部真相：牙人牟利成立但不知完整家族目的；初驗副記或等價來源能把故意放行接到官面意圖。
- 輸出：`broker_network_exposed`、`broker_status`、`clerk_intent_proven`。
- `E3_INTENT_LINK`：副記或等價雙來源建立意圖鏈 → 可承接第4階段，`active`。
- `E3_BROKER_ONLY`：只坐實牙人牟利 → 提早 `partly_completed (3/4)`。
- `E3_ABANDON`：放棄 → `failed`。

### 第4階段《重分渡權》｜已發布，末篇
- `script_id`: `ootb_campaign_mist_ferry_04_ferry_rights_20260902`
- 解鎖：第1 `scribe_exposed=true` AND 第2 `seal_source_known=true` AND 第3 `E3_INTENT_LINK`；由第3階段結算一次裁定並保存。
- NPC：#3、#4；#1/#2/#5按存檔可被引用，不要求存活或在場。
- 為何現在發生：意圖鏈逼近後，胥吏提前推動暫收渡權；代理申請在公開公告前送入。
- 局部目標：維持渡運、核對提前申請與內簿、完成責任與程序收束。
- 局部真相：胥吏利用自己促成的契據混亂推動家族利益，但書手、牙人仍各自承擔既有責任。
- `E4_ACCOUNTABLE`：責任鏈達標且代理提前承接被阻止 → `completed (4/4)`。
- `E4_PARTIAL`：保住渡運但責任鏈不足，或責任成立但程序未能當日完全恢復 → `partly_completed (4/4)`。
- `E4_FORCE_BREAK`：暴力使公開程序與合法收束失敗 → `failed (4/4)`。
- `E4_ABANDON`：放棄 → `failed (4/4)`。
- 末篇所有 ending 均直接收束，不再解鎖下一階段。

## 跨篇證物與代用品
- 半契：若遺失，第2階段只接受書手樣紙／紙料來源等前篇已成立代用品；若全無則不解鎖。
- 書手：可死亡、失蹤、拒絕；保存樣紙、腳夫供述與紙料採買記錄可替代其本人。
- 初驗副記：若毀損，第3階段可由同日初驗流水號、見證人、胥吏手記三者中至少兩項建立等價意圖鏈；第4階段只讀取第3階段已正式確認的等價鏈。
- 老船戶代表：若不可用，由普通船戶群體提供輪值與帳目，不繼承其個人記憶。
- 胥吏：若第4階段前已被拘留／不可用，其先前暫收提案、代理申請、內簿與收件簿繼續承載程序因果；不復活人物。

## 戰役收束矩陣
- 第1–3階段任一提早 ending：依各篇正式 ending 保存 `partly_completed/failed` 與當時 `campaign_progress`，不再自動續開。
- 第4 `E4_ACCOUNTABLE`：跨篇責任、程序與渡運形成完整收束，`completed (4/4)`。
- 第4 `E4_PARTIAL`：主要生活秩序有完成感，但官面意圖或程序結果只部分成立，`partly_completed (4/4)`。
- 第4 `E4_FORCE_BREAK/E4_ABANDON`：`failed (4/4)`。
- 每一桌的最終 NPC、證物、物品、官簿、謝儀與名譽結果以該篇正式結算寫入 `campaign_save`；總綱不追寫單桌結果。

## 戰役設計邊界
- 各階段不得把後篇真相倒灌成前篇自動資訊。
- 胥吏責任限於印樣外流、故意放行與利用爭議推動重分；不得改寫成全知主謀。
- 書手與牙人的既有責任後篇不得洗白。
- 玩家在任一非末篇真正切斷後續接口時，按該 ending 提早收束。
- 各階段的 DC、場景、整備、歷練、名譽、物質與結算均由各自 `.md` 完整提供；總綱不代檢單篇。