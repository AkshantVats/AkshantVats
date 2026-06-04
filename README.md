<div align="center">

# Akshant Sharma

### Staff Engineer building distributed systems, high-cardinality data planes, and open-source AI infrastructure.

[![Distributed Systems](https://img.shields.io/badge/Distributed%20Systems-111827?style=for-the-badge)](#)
[![AI Infrastructure](https://img.shields.io/badge/AI%20Infrastructure-0f766e?style=for-the-badge)](#)
[![Rust](https://img.shields.io/badge/Rust-000000?style=for-the-badge&logo=rust&logoColor=white)](#)
[![Kafka](https://img.shields.io/badge/Kafka-231f20?style=for-the-badge&logo=apachekafka&logoColor=white)](#)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-326ce5?style=for-the-badge&logo=kubernetes&logoColor=white)](#)
[![ClickHouse](https://img.shields.io/badge/ClickHouse-ffcc01?style=for-the-badge&logo=clickhouse&logoColor=111827)](#)

I work on the infrastructure layer underneath product features: ingestion engines, storage primitives, streaming pipelines, observability systems, and reliability controls that survive real traffic.

Currently building **Inferix**, an open-source AI infrastructure platform for inference observability, agent tracing, routing, drift detection, and retraining loops.

[LinkedIn](https://linkedin.com/in/akshantsharma07) · [Blog](https://akshantvats.github.io/Profile/blog/) · [Profile Site](https://akshantvats.github.io/Profile/) · [Email](mailto:akshant3@gmail.com)

</div>

---

## What I Am Building Now

### Inferix: self-hosted AI infrastructure, built in public

Teams shipping LLM features quickly run into the same production problems: high-cardinality inference events, hidden token spend, missing agent traces, routing regressions, quality drift, and retraining workflows that do not connect to production feedback.

I am building that stack as open source, one production-shaped component at a time.

```mermaid
flowchart LR
  apps["LLM apps / agents"] --> tracer["eBPF + SDK telemetry"]
  tracer --> ingest["Rust ingest edge"]
  ingest --> kafka["Kafka / Redpanda"]
  kafka --> clickhouse["ClickHouse analytics"]
  clickhouse --> console["Grafana / Inferix Console"]
  clickhouse --> route["routing + budgets"]
  clickhouse --> drift["drift detection"]
  drift --> retrain["fine-tuning pipeline"]
  retrain --> route
```

| Layer | Repo | What it proves |
|---|---|---|
| LensAI | [infra-ai-streaming](https://github.com/AkshantVats/infra-ai-streaming) | Rust ingest, WAL durability, Kafka, Go consumer, ClickHouse, Grafana, chaos tests |
| Zero-SDK tracing | [ebpf-llm-tracer](https://github.com/AkshantVats/ebpf-llm-tracer) | Kernel-level LLM HTTP tracing without app code changes |
| Execution system | [akshant-150-day-plan](https://github.com/AkshantVats/akshant-150-day-plan) | 150-day public build plan across LensAI, TraceForge, RouteIQ, DriftWatch, and FineForge |
| Writing + proof | [Profile](https://github.com/AkshantVats/Profile) | Technical posts connecting real production failures to AI infra design decisions |

---

## Flagship OSS

### [infra-ai-streaming](https://github.com/AkshantVats/infra-ai-streaming)

**Sub-100ms AI inference observability at 1M events/min: Kafka-backed, ClickHouse-native, multi-tenant.**

```text
Rust ingestion edge -> Kafka / Redpanda -> Go batch consumer -> ClickHouse -> Grafana
```

Built with:

- Rust/Axum HTTP ingest with WAL durability and per-tenant rate limits
- Kafka transport with channel-based backpressure
- Go consumer with ClickHouse batching, Redis overflow, circuit breaker, and DLQ
- Z-score latency anomaly detection per tenant and model
- Helm, k3d E2E, Grafana dashboards, Prometheus metrics, and chaos scenarios

The goal is not a toy demo. It is the kind of repo I would want to review in a serious infrastructure interview: architecture docs, tradeoffs, runbooks, benchmarks, failure modes, and deploy paths.

---

## 150-Day Public Build

I am running a 150-day execution plan to turn production infra experience into a coherent OSS AI infrastructure platform.

| Phase | Days | Product | Focus |
|---|---:|---|---|
| 1 | 0-29 | LensAI | Inference observability, cost metrics, ClickHouse analytics, eBPF telemetry |
| 2 | 30-59 | TraceForge | Agent traces, tool-call spans, replay, benchmark runner |
| 3 | 60-89 | RouteIQ | Semantic cache, prompt fingerprinting, budget routing, fallback chains |
| 4 | 90-119 | DriftWatch | Shadow traffic, judge evals, quality scoring, drift alerts |
| 5 | 120-149 | FineForge | Data prep, LoRA training, model registry, eval harness |

Each day ties three things together:

- code artifact: repo, design doc, benchmark, chart, test, or runbook
- AI infra learning: inference mechanics, routing, evals, agents, fine-tuning
- production memory: Agoda TSDB, Wayfair pricing, Delivery Hero logistics, Walmart IoT

That is the thesis: **real AI infrastructure is distributed systems work wearing a new API shape.**

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

## Recent Writing

- [Day 14: eBPF for AI Infrastructure](https://akshantvats.github.io/Profile/blog/series/ai-learning/day-14-ebpf-for-ai-infrastructure.html)
- [Profile blog](https://akshantvats.github.io/Profile/blog/)
- [150-day plan](https://github.com/AkshantVats/akshant-150-day-plan)

---

<div align="center">

### I am looking for Staff / Principal-level infrastructure roles where scale, reliability, and AI systems meet.

If your team cares about ingestion paths, storage engines, streaming systems, inference telemetry, or the reliability layer under AI products, we should talk.

[akshant3@gmail.com](mailto:akshant3@gmail.com) · [linkedin.com/in/akshantsharma07](https://linkedin.com/in/akshantsharma07)

<br/>

![Akshant's GitHub stats](https://github-readme-stats.vercel.app/api?username=AkshantVats&show_icons=true&theme=github_dark&hide_border=true&rank_icon=github)

</div>