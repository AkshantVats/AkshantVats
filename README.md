<div align="center">

![Inferix header](https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,50:0f766e,100:2563eb&height=190&section=header&text=Akshant%20Sharma&fontSize=44&fontColor=ffffff&animation=fadeIn&fontAlignY=36&desc=Distributed%20Systems%20%7C%20AI%20Infrastructure%20%7C%20Open%20Source&descSize=16&descAlignY=58)

# Akshant Sharma

### Software Engineer building distributed systems, high-cardinality data planes, and open-source AI infrastructure.

Nearly 9 years across Wayfair, Agoda, Delivery Hero, Walmart Labs, and Integration Wizards.

[![Distributed Systems](https://img.shields.io/badge/Distributed%20Systems-111827?style=for-the-badge)](#)
[![AI Infrastructure](https://img.shields.io/badge/AI%20Infrastructure-0f766e?style=for-the-badge)](#)
[![Rust](https://img.shields.io/badge/Rust-000000?style=for-the-badge&logo=rust&logoColor=white)](#)
[![Kafka](https://img.shields.io/badge/Kafka-231f20?style=for-the-badge&logo=apachekafka&logoColor=white)](#)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-326ce5?style=for-the-badge&logo=kubernetes&logoColor=white)](#)
[![ClickHouse](https://img.shields.io/badge/ClickHouse-ffcc01?style=for-the-badge&logo=clickhouse&logoColor=111827)](#)
[![Profile Views](https://komarev.com/ghpvc/?username=AkshantVats&style=for-the-badge&color=0f766e)](https://github.com/AkshantVats)

I work on the infrastructure layer underneath product features: ingestion engines, storage primitives, streaming pipelines, observability systems, and reliability controls that survive real traffic.

Currently building **[Inferix](https://github.com/AkshantVats/inferix)** — the control plane for agents and owned models: see every call, route by policy, catch quality drift, and retrain without guessing.

[LinkedIn](https://linkedin.com/in/akshantsharma07) · [Blog](https://akshantvats.github.io/Profile/blog/) · [Profile Site](https://akshantvats.github.io/Profile/) · [Email](mailto:akshant3@gmail.com)

<br/>

[`inferix`](#what-i-am-building-now) · [`flagship oss`](#flagship-oss) · [`live pulse`](#live-pulse) · [`experience`](#experience) · [`scale`](#production-scale-i-have-worked-on) · [`stack`](#stack) · [`contact`](mailto:akshant3@gmail.com)

</div>

---

## What I Am Building Now

### Inferix — the control plane for platform teams

Put agents and models behind one plane. See every call, route by policy, and catch quality drift. When quality drops, retrain and roll forward — without a second stack.

```mermaid
flowchart LR
  apps["Agents / apps / owned models"] --> plane["Inferix control plane"]
  plane --> lens["LensAI · see every call"]
  plane --> trace["TraceForge · agent graph"]
  plane --> route["RouteIQ · policy routing"]
  plane --> drift["DriftWatch · quality alerts"]
  drift --> forge["FineForge · retrain / promote"]
  forge --> route
```

| Product | Job | Repo |
|---|---|---|
| **LensAI** | See every call — latency, cost, tokens, errors | [lensai-integration](https://github.com/AkshantVats/lensai-integration) · [infra-ai-streaming](https://github.com/AkshantVats/infra-ai-streaming) · [ebpf-llm-tracer](https://github.com/AkshantVats/ebpf-llm-tracer) |
| **TraceForge** | Trace tools + model hops end to end | [agent-trace-collector](https://github.com/AkshantVats/agent-trace-collector) |
| **RouteIQ** | Route easy work to owned SLMs, hard work to strong paths | [routeiq](https://github.com/AkshantVats/routeiq) |
| **DriftWatch** | Alert when quality slips vs teacher / golden set | [driftwatch](https://github.com/AkshantVats/driftwatch) |
| **FineForge** | Retrain, promote, roll back | [fineforge](https://github.com/AkshantVats/fineforge) |

Suite map + how to start: **[github.com/AkshantVats/inferix](https://github.com/AkshantVats/inferix)** · Marketing site: **[inferix-web](https://github.com/AkshantVats/inferix-web)**

```bash
# Observe stack today (LensAI quickstart)
git clone https://github.com/AkshantVats/lensai-integration.git
cd lensai-integration && make up
```

---

## Flagship OSS

### [inferix](https://github.com/AkshantVats/inferix) — suite entrypoint

The umbrella repo for the five-product control plane. Start here to see how LensAI, TraceForge, RouteIQ, DriftWatch, and FineForge connect — then jump into the product repos.

| Product | Status | Repository |
|---|---|---|
| **LensAI** | Active | [lensai-integration](https://github.com/AkshantVats/lensai-integration) · [infra-ai-streaming](https://github.com/AkshantVats/infra-ai-streaming) · [ebpf-llm-tracer](https://github.com/AkshantVats/ebpf-llm-tracer) |
| **TraceForge** | Active | [agent-trace-collector](https://github.com/AkshantVats/agent-trace-collector) |
| **RouteIQ** | Scaffold → building | [routeiq](https://github.com/AkshantVats/routeiq) |
| **DriftWatch** | Scaffold → building | [driftwatch](https://github.com/AkshantVats/driftwatch) |
| **FineForge** | Scaffold → building | [fineforge](https://github.com/AkshantVats/fineforge) |

**Deepest production-shaped code today:** [infra-ai-streaming](https://github.com/AkshantVats/infra-ai-streaming) — Rust ingest → Kafka/Redpanda → Go consumer → ClickHouse → Grafana (WAL, backpressure, DLQ, chaos, Helm/k3d).

<div align="center">

[![inferix](https://github-readme-stats.vercel.app/api/pin/?username=AkshantVats&repo=inferix&theme=github_dark&hide_border=true)](https://github.com/AkshantVats/inferix)
[![infra-ai-streaming](https://github-readme-stats.vercel.app/api/pin/?username=AkshantVats&repo=infra-ai-streaming&theme=github_dark&hide_border=true)](https://github.com/AkshantVats/infra-ai-streaming)
[![agent-trace-collector](https://github-readme-stats.vercel.app/api/pin/?username=AkshantVats&repo=agent-trace-collector&theme=github_dark&hide_border=true)](https://github.com/AkshantVats/agent-trace-collector)
[![ebpf-llm-tracer](https://github-readme-stats.vercel.app/api/pin/?username=AkshantVats&repo=ebpf-llm-tracer&theme=github_dark&hide_border=true)](https://github.com/AkshantVats/ebpf-llm-tracer)

</div>

---

## Live Pulse

### Repo progress

<!-- LIVE_REPO_PULSE:START -->
| Repo | Stars | Forks | Open issues | Last push | Latest commit |
|---|---:|---:|---:|---:|---|
| [infra-ai-streaming](https://github.com/AkshantVats/infra-ai-streaming) | 0 | 0 | 4 | 1h ago | [`3b746c9`](https://github.com/AkshantVats/infra-ai-streaming/commit/3b746c9f7d8061aac4c18ec75ef9cf48c9ae206f) refactor: OSS polish days 87-90 (#161) |
| [ebpf-llm-tracer](https://github.com/AkshantVats/ebpf-llm-tracer) | 0 | 0 | 0 | 13d ago | [`4d3ce13`](https://github.com/AkshantVats/ebpf-llm-tracer/commit/4d3ce137097ecc9115a5b45ce01062716af02d5d) test: coverage improvements and GitHub Actions CI (#10) |
| [Profile](https://github.com/AkshantVats/Profile) | 1 | 0 | 0 | 9h ago | [`011df1d`](https://github.com/AkshantVats/Profile/commit/011df1d19f5526b7b89ac6cc3f250a5bdab492aa) sitemap+llms: Day 90 indexed |
<!-- LIVE_REPO_PULSE:END -->

### Latest writing

<!-- LATEST_BLOG_POSTS:START -->
- [Day 90 — Shadow Deployments for ML — Statistical Power](https://akshantvats.github.io/Profile/blog/series/ai-learning/day-90-shadow-deployments-statistical-power.html)
- [Day 90 — Netflix Shadow Traffic Talk — Applying to LLM Eval](https://akshantvats.github.io/Profile/blog/series/experience/day-90-netflix-shadow-traffic-llm-eval.html)
- [Day 89 — Product Thinking — Routers as Control Planes](https://akshantvats.github.io/Profile/blog/series/ai-learning/day-89-product-thinking-routers-control-planes.html)
- [Day 89 — Five Years of Infra Interviews — What “Staff” Signals Look Like](https://akshantvats.github.io/Profile/blog/series/experience/day-89-five-years-infra-interviews-staff-signals.html)
- [Day 88 — Launch Readiness — API Sandboxes and Rate Limits](https://akshantvats.github.io/Profile/blog/series/ai-learning/day-88-launch-readiness-api-sandboxes-rate-limits.html)
<!-- LATEST_BLOG_POSTS:END -->

### Recent public activity

<!-- RECENT_ACTIVITY:START -->
- `1h ago` opened PR [pull request in AkshantVats/infra-ai-streaming](https://github.com/AkshantVats/infra-ai-streaming)
- `1h ago` created branch in [AkshantVats/infra-ai-streaming](https://github.com/AkshantVats/infra-ai-streaming)
- `5h ago` pushed to [AkshantVats/akshant-150-day-plan](https://github.com/AkshantVats/akshant-150-day-plan): pushed commits
- `5h ago` pushed to [AkshantVats/akshant-150-day-plan](https://github.com/AkshantVats/akshant-150-day-plan): pushed commits
- `5h ago` created branch in [AkshantVats/akshant-150-day-plan](https://github.com/AkshantVats/akshant-150-day-plan)
- `8h ago` pushed to [AkshantVats/akshant-150-day-plan](https://github.com/AkshantVats/akshant-150-day-plan): pushed commits
<!-- RECENT_ACTIVITY:END -->

---

## Experience

| Company | Role | Tenure |
|---|---|---|
| **Wayfair** · Bengaluru | Sr. Software Engineer III · PAS & Pricing Promotions | Nov 2024 – Mar 2026 |
| **Agoda** · Bangkok | Sr. Software Engineer · Core Infrastructure · WhiteFalcon TSDB | Apr 2024 – Sep 2024 |
| **Delivery Hero** · Berlin | Sr. Software Engineer · Global Logistics Platform | Jun 2021 – Mar 2024 |
| **Walmart Labs** · Bengaluru | Software Engineer II · WeIoT SmartBuildings | Aug 2018 – May 2021 |
| **Integration Wizards** · Bengaluru | IoT Lead · Industrial IoT Platform | Mar 2017 – Aug 2018 |

**Highlights**

- **Wayfair** — GCP global pricing & promotion engine; hours → sub-seconds across 20k+ suppliers; 250k+ SKU updates/supplier at 99.99% availability.
- **Agoda** — WhiteFalcon TSDB at 1.5T events/day; cross-tier quantile queries; RoaringBitmap Kubernetes dimensions; Parquet Zstd cold tier.
- **Delivery Hero** — 1M+ daily orders on EKS; 5k+ route updates/sec via OSRM; async SQS + Kinesis status path.
- **Walmart Labs** — 7M+ sensors on Azure IoT Hub; HVAC Stream Analytics loops; edge-to-cloud OTA.
- **Integration Wizards** — IIoT ingestion for Dover USA; edge preprocessing in low-bandwidth environments.

---

## Production Scale I Have Worked On

| Scale | System | Stack |
|---:|---|---|
| 1.5T events/day | WhiteFalcon TSDB at Agoda | Rust, Scala, Kafka, Ceph, Redis, S3 |
| 7M+ sensors | Walmart SmartBuildings IoT platform | Azure IoT Hub, Stream Analytics, edge-to-cloud OTA |
| 5k geo-events/sec | Delivery Hero rider tracking | OSRM, AWS EKS, Kinesis, async pipelines |
| 250k+ SKU updates/supplier | Wayfair global pricing engine | GCP, Kafka, BigQuery, Redis, circuit breakers |
| 1M+ daily orders | Delivery Hero logistics platform | Kubernetes, SQS, Kinesis, distributed tracing |

I like the hard parts: cardinality, backpressure, quantiles, hot partitions, durability boundaries, failure isolation, cost-aware scaling, and the line where "just use a managed service" stops working.

---

## Engineering Taste

- Design docs before abstractions.
- Benchmarks with hardware context.
- Failure modes written down before production finds them.
- Backpressure over blind autoscaling.
- Per-tenant metrics over global averages.
- Runbooks, dashboards, and chaos tests as part of the product.

---

## Stack

<div align="center">

[![Stack](https://skillicons.dev/icons?i=rust,go,java,scala,python,kafka,kubernetes,docker,terraform,aws,gcp,azure,redis,postgres,prometheus,grafana)](#)

</div>

```text
Languages       Rust, Go, Java, Scala, Python
Streaming       Kafka, Redpanda, AWS Kinesis, Azure Event Hub
Storage         ClickHouse, Ceph, Redis, BigQuery, PostgreSQL, MongoDB, Parquet/S3
Infra           Kubernetes, Terraform, Helm, Docker, k3d
Cloud           AWS, GCP, Azure
Observability   OpenTelemetry, Prometheus, Grafana, ELK, distributed tracing
AI Infra        LLM inference pipelines, eBPF telemetry, evals, routing, cost controls
```

---

<div align="center">

### I am looking for Staff / Principal-level infrastructure roles where scale, reliability, and AI systems meet.

If your team cares about ingestion paths, storage engines, streaming systems, inference telemetry, or the reliability layer under AI products, we should talk.

[akshant3@gmail.com](mailto:akshant3@gmail.com) · [linkedin.com/in/akshantsharma07](https://linkedin.com/in/akshantsharma07) · [Inferix suite](https://github.com/AkshantVats/inferix)

<br/>

![Akshant's GitHub stats](https://github-readme-stats.vercel.app/api?username=AkshantVats&show_icons=true&theme=github_dark&hide_border=true&rank_icon=github)
![Top languages](https://github-readme-stats.vercel.app/api/top-langs/?username=AkshantVats&layout=compact&theme=github_dark&hide_border=true)

</div>
