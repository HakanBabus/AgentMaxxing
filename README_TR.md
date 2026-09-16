<div align="center">

# ⚡ AgentMaxxing

### Ana ajanı keskin tut. Ağır işi dışarı aktar.

**Codex tarzı coding workflow'lar için context-efficient delegasyon.**

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
![Status](https://img.shields.io/badge/status-experimental-orange)
![Workers](https://img.shields.io/badge/workers-LUNA-7c3aed)

[English](README.md) · [Türkçe](README_TR.md)

</div>

---

AgentMaxxing tek bir kural etrafında kurulmuş hafif bir orchestration skill'idir:

> **Ana ajan hedefi, kararları, kabul sürecini ve entegrasyon context'ini tutar. Ağır ve sınırları belli işler LUNA worker'lara gider.**

Main agent önce işin boyutunu değerlendirir. Tiny işler doğrudan yapılır, tek bounded sonuç bir LUNA'ya gidebilir, compound deliverable'lar ise dependency-aware ve kabul kapılı aşamalara ayrılır. Worker'lar küçük ve açık packet'lar alıp kısa, doğrulanabilir sonuçlar döndürür.

## Neden AgentMaxxing?

AgentMaxxing, **LUNA alt ajanları** üzerine kurulu ve pahalı main-agent context/token bütçesinde tasarruf hedefleyen bir orchestration modelidir. Main agent amacı, decomposition'ı, kararları ve kabul sürecini korur; LUNA `xhigh` veya `max` worker'lar bounded implementation, araştırma, validation ve correction context'ini taşır.

Amaç pahalı main-agent context'inin büyümesini azaltmak ve iş yükünün büyük bölümünü yüksek hacimli bir worker modele vermektir. Bu yaklaşım, dahilî Codex kullanım hakkından daha fazla odaklı iş çıkarmak isteyen **ChatGPT Plus** kullanıcıları için özellikle caziptir. OpenAI'ın [resmî Codex fiyatlandırma belgesi](https://learn.chatgpt.com/docs/pricing), Plus kapsamında Codex ile Luna dahil GPT-5.6 ailesini listeler ve Luna'yı hafif veya yüksek hacimli işler için daha yüksek kullanım seçeneği olarak tanımlar.

AgentMaxxing her görevde daha az toplam token garantisi vermez. Delegation, validation ve correction'ın da maliyeti vardır. Sistem, context'in nerede biriktiğini ve bounded işin büyük bölümünü hangi modelin yaptığını optimize eder.

| Katman | Sorumluluk |
| --- | --- |
| **Main agent** | İşi boyutlandırır, stage map hazırlar, net packet'lar yazar ve `ACCEPT` veya `REJECT` kararı verir |
| **LUNA filosu** | Bounded aşamaları `xhigh` veya `max` ile uygular, self-review ve validation yapar, reddedilen işi düzeltir |
| **Evidence handoff** | Raw log veya bütün worker context'i yerine acceptance kanıtı ve compact sonuç döndürür |
| **Acceptance gate** | Önkoşulları açıkça kabul edilmeden bağımlı aşamaları kilitli tutar |

Sabit bir worker limiti yoktur. LUNA'nın düşük marjinal maliyeti faydalı delegasyon eşiğini düşürür. Worker sayısını gerçek stage ownership ve validation sınırları belirler. Yalnızca eşzamanlı worker'ların bağımsız olması gerekir; sıralı aşamalar, önkoşulları kabul edildikten sonra fresh worker'lara verilebilir.

## Neden doğrudan LUNA kullanmıyoruz?

Tek, küçük ve bounded bir görevde düz LUNA oturumu hâlâ en basit seçenektir. İstek compound, uzun süreli, kalite hassasiyetli veya tek worker context'ini aşabilecek durumdaysa AgentMaxxing daha faydalı hâle gelir.

| Düz LUNA oturumu | AgentMaxxing |
| --- | --- |
| Tek worker bütün hedefi ve execution geçmişini taşır | Main hedefi tutar; worker'lar yalnızca kendi aşamalarının context'ini alır |
| Geniş bir şartname tek overloaded göreve dönüşebilir | Compound iş dependency-aware ve kabul kapılı aşamalara ayrılır |
| Implementation yapan worker aynı zamanda temel değerlendiricidir | Main açık acceptance gate uygular; geniş final-quality iddiaları fresh evaluator alabilir |
| Hata genellikle geniş bir retry üretir | Red, işin sahibi worker'a dar bir correction packet olarak döner |
| Context tek uzun oturumda büyür | Ağır implementation ayrıntıları compact handoff'ların arkasında izole kalır |

Avantaj, LUNA'nın farklı bir modele dönüşmesi değildir. LUNA daha temiz görevler alır, daha küçük context'lerde çalışır ve eksik işin ilerlemesine izin vermeyen bir integration owner tarafından denetlenir.

## Routing

| İş | Varsayılan rota |
| --- | --- |
| Küçük veya sıkı bağlı task | Main doğrudan yapar |
| Tek ağır ve bounded task | Tek LUNA worker |
| Compound deliverable | Dependency-aware stage map hazırla |
| Sıralı aşamalar | Sonraki kabul edilmiş aşamaları fresh worker'lar üstlenebilir |
| Bağımsız iş akışları | Çakışmayan LUNA worker'ları paralel çalıştır |
| Geniş final-quality iddiası | Fresh, read-only end-to-end evaluator kullan |

Çakışan dosya sahipliğinden, tekrarlanan repo keşfinden ve somut gerekçe olmadan worker'a bütün konuşmayı vermekten kaçın.

## İş boyutlandırma

İşin boyutunu istenen dosya, klasör, repository veya final artefact sayısından çıkarma. Tek bir çıktı bile birkaç gerçek aşama içerebilir.

Şunlardan birkaçını bir araya getiren işleri compound kabul et:

- subsystem, package, surface, audience veya deliverable türleri;
- discovery, architecture, implementation, content, migration, polish ve validation;
- user flow, platform, environment veya operating mode;
- objective correctness ile subjective quality;
- birbirinden farklı validation yöntemleri;
- complete, final, polished veya production-ready olarak tarif edilen greenfield ya da end-to-end sonuç.

Compound işlerde main compact bir stage map hazırlar. Her aşama; tek bounded outcome, dependency, worker ownership, `xhigh` veya `max` effort, write scope, ölçülebilir acceptance, validation ve o packet'ın dışında bırakılan sonraki işleri içerir.

Detaylı requirements, overloaded bir görevi bounded yapmaz. Bir aşamadaki düzeltmeler için aynı worker'ı kullan; sonraki kabul edilmiş aşamanın hedefi, context'i veya validation yüzeyi değişiyorsa normalde fresh worker aç.

## Sorumluluklar

### Main agent

Main agent şunların sahibidir:

- kullanıcı amacı ve kısıtları;
- mimari kararlar;
- task decomposition ve worker ownership;
- workload sizing ve compact stage map;
- çakışma tespiti;
- final entegrasyon ve doğrulama;
- delege edilen aşamalar için açık `ACCEPT` veya `REJECT` kararı;
- final cevap.

### LUNA worker

Bir LUNA worker tek bir bounded sonucun sahibidir. Şunları yapmalıdır:

1. yalnızca gerekli girdileri incelemek;
2. işi verilen scope içinde tamamlamak;
3. ilgili doğrulamaları çalıştırmak;
4. self-review yapıp bulduğu bütün önemli sorunları düzeltmek;
5. her kabul kriterini kısa kanıtla eşlemek;
6. compact handoff ile `ready-for-review` dönmek.

Mümkün olduğunda reasoning profili:

```text
model: gpt-5.6-luna
reasoning: xhigh | max
```

Stabil interface'lere ve doğrudan validation'a sahip bounded işlerde **xhigh** kullan. Birden fazla sistemi etkileyen implementation, architecture-heavy işler, UI/input/render etkileşimi, nondeterministic hata ve pahalı regression riskinde **max** kullan. xhigh aynı önemli gereksinimi tekrar tekrar kaçırırsa görevi yeniden çerçevele veya gerçek sınırlardan böl; yalnızca gerekli correction context'ini fresh bir max worker'a ver.

Tek bounded aşamada independent review opsiyoneldir. Geniş end-to-end veya final quality iddiası taşıyan compound işlerde fresh bir LUNA evaluator, kabul edilmiş aşamaları write ownership almadan birlikte doğrulamalıdır. Kusurlar etkilenen aşamanın sahibi worker'a geri döner.

## Worker packet

Delegasyondan önce belirsizliği kaldır. Kullanışlı bir packet şu şekildedir:

```markdown
Role: LUNA worker

Reasoning:
xhigh | max

Stage:
<stage ID ve bounded outcome>

Depends on:
<kabul edilmiş prerequisite ID'leri veya none>

Goal:
<tek ve somut sonuç>

Why delegated:
<izole kalması gereken ağır context veya iş yükü>

Inputs:
- <tam dosya, klasör, log, komut, URL veya artefact>

Scope:
- May inspect: <...>
- May edit: <...>
- Must not edit: <...>

Later stages / not this task:
- <bu packet'ın dışında bırakılan sonraki işler>

Suggested steps:
1. <ilk faydalı adım>
2. <doğrulama ve self-review>

Constraints:
- <davranış, API, dependency, stil veya izin sınırı>

Done when:
- A1 — <ölçülebilir kabul kriteri>
- A2 — <ölçülebilir kabul kriteri>

Critical review surfaces:
- <main'in kontrol edeceği integration boundary, riskli davranış veya artefact>

Validation:
- <tam komut veya kontrol>

Return only:
- status
- changed files
- 2–5 result bullets
- her kriter için acceptance evidence
- validation result
- self-review result
- material caveat or decision needed
```

Edge case'ler için [worker packet rehberine](.agents/skills/agentmaxxing/references/worker-packet.md) ve [routing rehberine](.agents/skills/agentmaxxing/references/routing.md) bakabilirsin.

## Compact handoff

Worker transcript değil, entegrasyon indeksi döndürmelidir:

```text
STATUS: ready-for-review | needs-input | failed

CHANGED:
- <paths or none>

RESULT:
- <2–5 kısa madde>

ACCEPTANCE:
- A1 PASS/FAIL — <kısa kanıt>
- A2 PASS/FAIL — <kısa kanıt>

VALIDATION:
- PASS/FAIL/SKIPPED — <tam komut veya kontrol>

SELF-REVIEW:
- <düzeltilen önemli sorun veya none>

CAVEAT / DECISION NEEDED:
- <yalnızca önemliyse>
```

Main agent yalnızca entegrasyon için gereken diff veya artefact'ları açar.

## Kabul ve düzeltme

Main agent karar vermek için changed path listesini, acceptance evidence'ı, zorunlu validation'ı, önceden belirtilen kritik yüzeyleri ve yalnızca entegrasyon açısından hassas diff veya artefact'ları kontrol eder.

- Bütün zorunlu kriterlerin güvenilir kanıtı varsa ve önemli sorun es geçilmiyorsa **ACCEPT**.
- Kanıt eksikse, validation yetersizse, scope dışına çıkılmışsa veya önemli kusur kalmışsa **REJECT**.

Red durumunda main agent; başarısız acceptance ID'lerini, gözlenen kanıtı, korunacak çalışan davranışı, correction scope'u ve tam recheck'i aynı LUNA worker'a gönderir. LUNA bir delta handoff döndürür ve main agent yeniden karar verir. Kabul edilene veya gerçek bir authorization, kullanıcı kararı ya da external-state engeline ulaşılana kadar döngü sürer. Main agent kriteri es geçmez, reddedilen delegated implementation'ı sessizce kendisi düzeltmez ve bağımlı aşamayı açmaz.

## Kurulum

Repo-scoped skill şu konumdadır:

```text
.agents/skills/agentmaxxing/
```

Codex skill installer ile kur veya bu klasörü desteklenen bir skills konumuna kopyala. Açıkça çağır:

```text
$agentmaxxing <repo görevin>
```

Implicit invocation kapalıdır; böylece küçük normal işler workflow'u istemeden değiştirmez.

## Repo yapısı

```text
AgentMaxxing/
├── .agents/skills/agentmaxxing/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   └── references/
│       ├── routing.md
│       └── worker-packet.md
├── docs/ARCHITECTURE.md
├── AGENTS.md
├── CHANGELOG.md
├── README.md
└── README_TR.md
```

AgentMaxxing bir runtime değil, instruction layer'dır. Daemon, database, telemetry servisi, token ledger veya persistent task registry içermez.

## VisionOffload

VisionOffload şimdilik bilerek dahil edilmedi. Ayrı geliştirilecek ve daha sonra aynı context-isolation prensiplerini kullanabilecek.

## Lisans

Apache License 2.0. AgentMaxxing bağımsız bir açık kaynak projesidir; OpenAI ile bağlantılı veya OpenAI tarafından onaylanmış değildir.
