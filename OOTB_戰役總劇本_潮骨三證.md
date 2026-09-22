# 《潮骨三證》戰役總劇本

## 規格頭
- 戰役名：潮骨三證
- `campaign_id`：`ootb_campaign_tidebone_three_proofs`
- 總劇本版本：1.0.3
- 戰役狀態：連載中
- 已正式發布的階段劇本：無
- 當前規劃階段：四階段；第一至第三階段在 `campaign_in_progress` 撰寫／修訂中，第四階段規劃中
- 共同起點：西海道海陵外港、蒼龍灣東緣鹽埠
- 主要地理範圍：海陵外港、蒼龍灣近岸礁島、鹽運支渠與舊船塢；均屬西海道地方新增地點，不改寫定潮島與海陵既有權威設定
- 建議等級走向：6–10級；各階段以 R8 為主要校準
- 共用世界權威：`世界知識庫/地理與世界基準/時代與世界基準.md`、`世界知識庫/地理與世界基準/昊國地理.md`
- repository 與桌次分工：本檔固定作者層跨篇真相、NPC registry、state 與接口；單桌實際姓名、傷亡、取得證物及已宣告承接結果由 `campaign_save` 保存，不回寫本檔。

## 跨篇核心答案
海陵外港近月連續出現「退潮後鹽貨受潮、驗潮木樁刻度錯位、舊船塢夜間有空船移位」三類表面互不相干的異常。根本原因是地方鹽運承包人利用一條已廢棄但仍通水的船塢側渠，在退潮窗口把未報關的高價海貨轉入內港，再以鹽貨損耗與潮汐誤差掩蓋重量與船位差額。

這不是海關、水師、蒼龍門或任何既有正式組織的共同陰謀。主要策劃者是一名地方承包人；他買通一名外港驗潮書吏修改潮簿，並以債務控制一名舊船塢領工安排夜間絞盤與閘板。三人利益並不一致：承包人求長期私運利潤；書吏求償債並害怕罪責；領工最初只求保住欠薪工人的飯碗，後來發現貨物價值遠超承包人所稱的「避稅雜貨」，開始暗留實物記號自保。

戰役開始前已成立：側渠可在特定退潮窗口通行小艇；三人已完成至少三次私運；潮簿已有系統性改寫；領工已暗留三枚不同批次的船釘作日期記號。尚未發生：策劃者是否滅證、書吏是否倒戈、領工是否公開記號、最後一次大批貨是否成功轉走；這些只按玩家造成的 state 觸發。

## 跨篇真實時間線
1. 六個月前：地方承包人發現舊船塢側渠在低潮仍可通小艇，開始測試。
2. 四個月前：承包人以債務與分成拉攏驗潮書吏，建立「潮簿延後半刻、貨重以受潮折耗沖帳」的做法。
3. 三個月前：舊船塢領工被要求夜間調整絞盤；他相信只是規避部分稅費，接受額外工錢。
4. 一個月前：領工看見密封海貨箱與護送者，懷疑事情更大，開始用三枚不同鍛痕船釘記錄三次異常夜班。
5. 戰役開始：一批鹽貨在不應受潮的位置出現海水線，地方鹽商要求查清損耗。
6. 玩家不介入：書吏繼續改簿；承包人於十日內完成最後一批大貨後封死側渠；領工若察覺滅證風聲會帶一枚船釘逃離，其餘證據可能被焚。

## 跨篇主要行動者
### `actor_contractor`／<NPC#1@戰役:潮骨三證: 姓?-名?>
- 身份：外港鹽運地方承包人；跨篇主要策劃者。
- 初始知道：側渠用途、每次私運窗口、書吏與領工的角色、最終大貨日期。
- 不知道：領工已留船釘記號；玩家能否從鹽貨水線反推側渠。
- 核心利益：保住承包權與私運利潤，避免正式官署取得完整證據鏈。
- 當前計畫：完成最後一批大貨後封渠、銷毀舊絞盤帳。
- 資源：地方腳夫、租用倉棚、數名受薪護貨人；無權調動海關、水師或蒼龍門。
- 限制：不能公開使用暴力而不引來官署；帳目需與潮簿相互吻合。
- 反應：`state_ledger_exposed=true` 時提前轉移大貨；`state_foreman_cooperates=true` 時嘗試收買或隔離領工；身份公開且證據鏈完整時優先逃離而非死戰。

### `actor_clerk`／<NPC#2@戰役:潮骨三證: 姓?-名?>
- 身份：外港驗潮書吏。
- 初始知道：哪些潮簿被改、承包人支付方式、部分夜班日期。
- 不知道：貨物真正種類、領工的船釘記號、最後大貨完整路線。
- 核心利益：償債、免罪、保住家人生活。
- 當前計畫：繼續按指示改簿，同時保留一張私人對潮草紙防止被滅口。
- 資源：潮簿接觸權、值房鑰匙、熟悉潮汐記錄。
- 限制：膽小，沒有武力班底；一旦相信承包人會棄他便可能倒戈。
- 反應：玩家提出兩項互相獨立的帳實矛盾且允諾交官時陳情，會交出私人草紙；遭公開羞辱或無證威脅則先逃。

### `actor_foreman`／<NPC#3@戰役:潮骨三證: 姓?-名?>
- 身份：舊船塢領工。
- 初始知道：絞盤、側渠、三次夜班與實物箱；不知道承包人的完整買家網。
- 核心利益：保護欠薪工人、避免自己成替罪羊、留下自保證據。
- 當前計畫：藏好三枚船釘，觀察承包人是否準備滅證。
- 資源：船塢地形、工人信任、絞盤操作知識。
- 限制：若工人被扣薪或拘捕，他會優先救人。
- 反應：玩家能證明願意區分工人與策劃者責任時合作；若玩家直接焚毀船塢或無差別抓工人則撤走證物並拒絕協助。

### `actor_buyers`
- 身份：尚未固定為任何 Handbook 既有組織的外海買家網；只作戰役局部真相中的交易對手。
- 利益：按約收貨，避免身份曝光。
- 資源：一艘可在灣外接貨的中型商船與短期僱工。
- 限制：不願為地方承包人與官府正面衝突。
- 反應：若最後交貨點曝光，會棄約離開；不自動升格成跨戰役母勢力。

## 戰役級 NPC registry
| Key | 姓名欄 | 身份／功能 | actor_key | 首次規劃登場 | 首次正式登場 |
|---|---|---|---|---|---|
| `NPC#1@戰役:潮骨三證` | 姓?-名? | 鹽運承包人／策劃者 | `actor_contractor` | 第一階段 | 待發布 |
| `NPC#2@戰役:潮骨三證` | 姓?-名? | 驗潮書吏／帳簿接口 | `actor_clerk` | 第一階段 | 待發布 |
| `NPC#3@戰役:潮骨三證` | 姓?-名? | 舊船塢領工／實物接口 | `actor_foreman` | 第一階段 | 待發布 |

編號永久保留；新增跨篇具體人物須先更新本表。

## Campaign state registry
| state_key | 型別／可用值 | 首次建立來源 | 世界事實 | 後續讀取與實際效果 |
|---|---|---|---|---|
| `state_ledger_exposed` | boolean | 第一階段 | 潮簿改寫是否已成為可用證據並已使承包人知道帳線受威脅 | 第二階段決定護貨人是否提早到場，並與本篇耗時共同決定 `state_final_cargo` 是否寫成 `moved_early`；第三階段決定B是否可直接引用前篇帳證 |
| `state_clerk_status` | `active / cooperating / fled / detained / dead` | 第一階段 | <NPC#2@戰役:潮骨三證> 的可接觸狀態 | 第二階段決定是否能直接取得兩個夜班日期；第三階段 `cooperating` 時提供半刻級潮時優勢，其餘狀態不得被重置 |
| `state_foreman_status` | `active / cooperating / hostile / fled / detained / dead` | 第一階段 | <NPC#3@戰役:潮骨三證> 的可接觸狀態 | 第二階段決定接觸方式與藏釘替代路徑；第三、四階段決定本人可否提供水道／證詞，缺席時使用已寫明代用品 |
| `state_foreman_cooperates` | boolean | 第二階段 | 領工是否正式同意按證據區分工人責任並協助玩家 | 第三階段為 true 時直接提供兩個觀察點與岸上備用路；第四階段只作證人／水道資源，不作解鎖硬前提 |
| `state_spike_count` | integer `0..3` | 第二階段 | 玩家已取得並保全的船釘日期記號數 | 第三階段 `>=2` 時可把三次夜班作為B的既有獨立歷史佐證；`0..1` 時仍須靠潮位、領工／船夫或現場移貨補足 |
| `state_side_channel` | `unknown / located / secured / destroyed` | 第一階段可提前建立，第二階段正式更新 | 側渠的已知與物理狀態 | 第三階段直接決定貨走側渠、先破封鎖或改走岸上短駁；第四階段只讀其留下的地方證據，不令側渠復原 |
| `state_final_cargo` | `scheduled / moved_early / intercepted / escaped / unresolved` | 第二階段先建立 `scheduled/moved_early`；第三階段更新 | 最後一批貨的時間／去向狀態 | 第三階段以 `scheduled/moved_early` 決定開場倒數；第四階段只在第三階段已解鎖時讀取 `intercepted/escaped` 與相應後果；放棄而未能確認去向時記 `unresolved` |
| `state_contractor_status` | `active / exposed / fled / detained / dead` | 第三階段 | <NPC#1@戰役:潮骨三證> 的公開／人身狀態 | 第三階段決定本人是否現場；第四階段決定是否由本人、帳冊／租約或護貨人口供承接責任鏈 |
| `state_buyer_route` | `unknown / partial / confirmed` | 第三階段 | 玩家對灣外接貨路線的可追程度 | 第四階段解鎖硬前提之一：`confirmed` 對應完整接口，`partial/confirmed` 可對應追索接口；`unknown` 令第四階段保持鎖定 |
| `campaign_status` | `active / partly_completed / failed / completed` | 第一階段每次正式結算 | 本桌整條戰役的當前層級結果 | 每篇結算只依該 ending 固定一次；`active` 才可保存下一階段接口，`partly_completed/failed/completed` 均不再自動承接 |
| `campaign_progress` | `0/4 / 1/4 / 2/4 / 3/4 / 4/4` | 第一階段每次正式結算 | 已正式結算的階段數／本版規劃總階段數 | 玩家可見戰役收束與 campaign_save 顯示使用；不作後篇解鎖的替代條件 |

只有以上真正被後篇讀取或需要保存戰役層結果的資料進入 campaign state；第一階段「已確認海水來源」屬本篇已結算事實，不另保留一個後篇不讀取的旗標。

### 戰役初始 state
正式開始第一階段、尚未結算任何 ending 時，`campaign_save` 的作者層基線為：
- `state_ledger_exposed=false`
- `state_clerk_status=active`
- `state_foreman_status=active`
- `state_foreman_cooperates=false`
- `state_spike_count=0`
- `state_side_channel=unknown`
- `state_contractor_status=active`
- `state_buyer_route=unknown`
- `campaign_status=active`
- `campaign_progress=0/4`
- `state_final_cargo` 尚未建立；只在第二階段正式結算時首次寫入 `scheduled/moved_early`，不得提前用預設值覆蓋實際時間線。

## 承接裁決共通規則
- 每個非末篇可承接 ending 只在該篇正式結算時，依本總綱、current `campaign_save` 與本篇凍結結果判定一次完整解鎖路線。
- 成立時保存 `continuation_status=open`、目標 `next_stage` 與實際匹配的完整路線；下一篇開局只載入這個 `continuation_handoff`，不得重新計算前篇能否承接。
- 不可承接／放棄時保存 `continuation_status=closed`、`next_stage=none`，並依下列提早戰役結局寫入 `partly_completed` 或 `failed`。
- repository 之後改版不得追溯改判已由某桌正式宣告並保存的承接結果。

## 四階段接口
### 第一階段《鹽袋上的第二道水線》
- 狀態：撰寫中；branch 內已完成 1.0.3 修訂，未正式發布。
- 輸入：戰役共同起點；無前篇要求。
- 使用 NPC：#1、#2、#3。
- 為何現在發生：鹽貨出現不合正常堆放位置的第二道海水線，承包人要求以「倉漏」結案。
- 玩家介入：受損鹽商共同出資請江湖人先查清，以免與官署爭議前失去貨證。
- 獨立目標：找出鹽貨受潮的直接原因、保全貨證並判斷是否存在人為帳實差。
- 局部真相：一批鹽袋曾在夜間經側渠小艇轉運後回填原倉；書吏配合改了潮時。
- 可改 state：`state_ledger_exposed`、`state_clerk_status`、`state_foreman_status`；若玩家提前找到側渠，可提前建立 `state_side_channel`。
- 主要 ending：
  - `E1_chain_intact`：水線與潮簿兩條證據都成立；`campaign_status=active`，解鎖第二階段。
  - `E1_physical_only`：只保住實物因果，潮簿證據未成；`campaign_status=active`，第二階段以船塢物證路線開場。
  - `E1_false_closure`：接受倉漏說且正式結案，玩家沒有可追接口；`campaign_status=partly_completed`、`campaign_progress=1/4`。最終保存 `state_ledger_exposed=false`、書吏／領工實際 status、若已提前找到則保存 `state_side_channel`；貨證依結算移交鹽商。戰役收束《潮痕止於倉門》：眼前賠付完成、鹽貨爭議結束；尾聲只呈現下一次退潮時遠處舊船塢傳來一次不合班次的絞盤聲。因沒有A+C或A+B可承接證據組合，原第二階段不再自動發生；GM 宣告「戰役部分完成（1/4）」。
  - `E1_abandon`：放棄；`campaign_status=failed`，戰役終止。
- 第二階段解鎖：
  - 路線A（來源：第一階段）：`E1_chain_intact` 已結算為可承接；帳實矛盾令「為何現在」成立，玩家以受委託調查者身分追到舊船塢。
  - 路線B（來源：第一階段）：`E1_physical_only` 已結算為可承接；船脂、麻纖維與搬運方向令「為何現在」成立，玩家以保全貨證的延伸調查者身分介入。
  - A OR B 即可；`state_clerk_status`、`state_foreman_status`、`state_side_channel` 只改開場差異，不是額外解鎖門檻。若兩個 ending 均不成立，第二階段保持鎖定。

### 第二階段《三枚不同鍛痕的船釘》
- 狀態：撰寫中；branch 內已完成 1.0.3 修訂，未正式發布。
- 輸入：第一階段可承接 ending；帶入書吏與領工狀態。
- 使用 NPC：#1、#2、#3。
- 為何現在發生：第一階段留下的潮時／實物矛盾指向舊船塢；領工開始擔心自己被滅證。
- 玩家介入：追查可驗證第一階段結論的實物來源，或依領工留下的間接訊息赴船塢。
- 獨立目標：確認夜班絞盤用途、找出側渠位置、決定如何處理領工與工人。
- 局部真相：三枚船釘是領工對三次夜班的日期記號；絞盤用來在退潮時移動小艇閘板。
- 可改 state：`state_foreman_status`、`state_foreman_cooperates`、`state_spike_count`、`state_side_channel`，並依第一階段帳線與本篇耗時先建立 `state_final_cargo=scheduled/moved_early`。
- 主要 ending：
  - `E2_route_proven`：定位側渠且至少保住一枚船釘；`campaign_status=active`，解鎖第三階段。
  - `E2_foreman_deal`：未取得完整物證但領工合作並口述操作法；`campaign_status=active`，第三階段以人證監視路線開場。
  - `E2_workers_broken`：玩家無差別處置工人，領工帶證逃離且側渠未定位；`campaign_status=partly_completed`、`campaign_progress=2/4`。最終保存 `state_foreman_status=hostile/fled` 依實際、`state_foreman_cooperates=false`、`state_spike_count` 已保全數量、`state_side_channel=unknown`，並保留第一階段所有有效 state；本篇未建立可承接的最後貨接口。收束《船塢只剩斷索》：本篇工人衝突正式處理，第一階段貨損仍可交差；因既無側渠位置／用途證據亦無合作領工，第三階段不開。GM 宣告「戰役部分完成（2/4）」。
  - `E2_abandon`：放棄；`campaign_status=failed`。
- 第三階段解鎖：
  - 路線A（來源：第二階段＋第一階段差異）：`E2_route_proven` 可承接；第二階段已證明側渠／夜班用途。第一階段的 `state_ledger_exposed`、`state_clerk_status` 不作門檻，但分別改變帳證來源與潮時資訊。
  - 路線B（來源：第二階段＋第一階段差異）：`E2_foreman_deal` 可承接且 `state_foreman_cooperates=true`；領工的人證與觀察點令最後貨監視有實際入口。第一階段 state 同樣只改開場差異。
  - A OR B；兩條路線都必須帶入第二階段已結算的 `state_final_cargo` 及全部仍有效早期 state。若兩個 ending 均不成立，第三階段保持鎖定。

### 第三階段《退潮前移動的最後一批貨》
- 狀態：撰寫中；branch 內已完成 1.0.3 修訂，未正式發布。
- 輸入：第二階段可承接 ending；同時讀取第一階段 `state_ledger_exposed`、`state_clerk_status`。
- 使用 NPC：#1、#2、#3。
- 為何現在發生：承包人按暴露程度選擇原定交貨或提前轉移最後一批貨。
- 玩家介入：由側渠／領工人證推知下一次退潮窗口，可監視、截貨、跟蹤或促使書吏合作。
- 獨立目標：確認最後貨物的移動路線並取得足以指向承包人的責任鏈。
- 局部真相：最後一批貨是策劃者準備收尾的最大一批；外海買家只按約接貨，不會為他死守。
- 條件式開場：直接讀取第二階段已結算的 `state_final_cargo`；`moved_early` → 貨物提前一個潮窗，`scheduled` → 按原定窗口。只有舊存檔缺少此鍵時才以 `state_ledger_exposed`／第二階段耗時作相容補寫。`state_clerk_status=cooperating` → 玩家可取得半刻級潮時資訊；否則須靠船塢觀察。
- 可改 state：`state_final_cargo`、`state_contractor_status`、`state_buyer_route`。
- 主要 ending：
  - `E3_chain_to_buyer`：取得承包人責任鏈並確認外海接貨路線；`campaign_status=active`，解鎖第四階段。
  - `E3_contractor_only`：承包人責任成立但買家路線永久失去；`campaign_status=partly_completed`、`campaign_progress=3/4`、`state_buyer_route=unknown`，並保存 `state_final_cargo` 與 `state_contractor_status` 的實際最終值。收束《潮口止證》：地方私運案可正式交辦、貨路在海面斷掉；尾聲只留下無主接貨燈號熄滅。因沒有可靠灣外路線可追，第四階段不開；GM 宣告「戰役部分完成（3/4）」。
  - `E3_cargo_escaped_with_trace`：貨逃走但玩家取得可靠船向／燈號；`state_buyer_route` 依一項未交叉核對資料=`partial`、兩項以上相容獨立資料或可核對木牌=`confirmed`；`campaign_status=active`，第四階段改為追索路線。
  - `E3_abandon`：放棄；`campaign_status=failed`。
- 第四階段解鎖：
  - 路線A（來源：第三階段，並保留第一／二階段差異）：`E3_chain_to_buyer` AND `state_buyer_route=confirmed`；玩家已握有可直接辨認的灣外接貨接口。
  - 路線B（來源：第三階段，並保留第一／二階段差異）：`E3_cargo_escaped_with_trace` AND `state_buyer_route=partial/confirmed`；玩家以可靠船向／燈號／礁位追索。
  - A OR B；`state_final_cargo`、`state_contractor_status`、`state_foreman_cooperates`、`state_side_channel` 不另作解鎖門檻，但必須帶入並改變末篇開場、可用證人與貨物狀態。若 `state_buyer_route=unknown` 或第三階段 ending 不屬上述兩者，第四階段保持鎖定並由第三階段完成提早收束。

### 第四階段《灣外沒有名字的接貨燈》
- 狀態：已規劃、未製作。
- 輸入：第三階段可承接 ending；讀取 `state_final_cargo`、`state_contractor_status`、`state_buyer_route`、`state_foreman_cooperates`。
- 使用 NPC：#1（若仍可接觸）；#2/#3只按既有狀態作證人或缺席，不強制存活。
- 為何現在發生：玩家已取得外海接貨路線或可追蹤痕跡，買家船準備離開蒼龍灣。
- 玩家介入：追索最後貨／交易證據，或把完整證據鏈交給有權機關處理並協助辨認接貨船。
- 獨立目標：處理最後一批貨與外海交易接口，決定證據、貨物與地方責任人的最終交付。
- 局部真相：買家網只是一組逐利交易者，不揭露為既有大勢力；其離開不會無限延伸新陰謀。
- 末篇規劃 ending：
  - `E4_full_delivery`：截獲或完成合法證據交辦，核心因果與最後貨接口均處理；`campaign_status=completed`、`campaign_progress=4/4`。
  - `E4_bitter_close`：買家船離開，但地方責任鏈、最後貨去向與接貨接口已獲足夠處理，主要問題可正式回答；`campaign_status=completed`、`campaign_progress=4/4`，以苦澀完成收束。
  - `E4_abandon`：玩家明確退出末篇核心追索；依戰役規則一律 `campaign_status=failed`、`campaign_progress=4/4`，保留前三篇既有成果但不把放棄改寫為 `partly_completed`。第四階段正文製作時必須把三者落成可直接運行的完整 ending。

## 跨篇一致性與回歸代用品
- #1 死亡／被捕：後篇以其帳冊、租約、受薪護貨人口供承接責任鏈；不得讓死亡抹掉已存在的客觀證據。
- #2 死亡／失蹤：私人對潮草紙若此前未取得，第三階段失去潮時捷徑，但仍可由船塢潮痕與現場監視推進。
- #3 死亡／失蹤：已取得船釘照常有效；若一枚未得，側渠本體與絞盤磨痕仍可提供獨立來源。
- 側渠被毀：毀損本身留下新鮮封堵、泥沙與工具痕跡；第三階段改用岸上轉運監視，不重置成「從未存在」。
- 玩家提前公開案情：承包人按 `state_ledger_exposed` 類型提前移貨；不保證預定場景照常發生。

## 最終收束邊界
第四階段必須讓玩家接觸並處理戰役根本因果：地方承包人如何利用潮時、側渠、帳簿與工人完成私運，以及外海接貨接口如何終止。外海買家不升格成新的無限幕後黑手；若其身份未明，可作「局部未盡答案」，但戰役仍須對地方私運結構、主要責任人、最後貨物與證據交付作正式結算。
