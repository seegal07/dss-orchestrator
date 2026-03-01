CREATE TABLE runs (
  run_id UUID PRIMARY KEY,
  created_at TIMESTAMPTZ NOT NULL,
  updated_at TIMESTAMPTZ NOT NULL,
  status TEXT NOT NULL,
  current_state TEXT NOT NULL,
  request_hash CHAR(64) NOT NULL,
  version_anchor TEXT NOT NULL,
  owner_gate_required BOOLEAN NOT NULL,
  owner_gate_approved BOOLEAN NOT NULL DEFAULT FALSE,
  owner_gate_approved_at TIMESTAMPTZ NULL,
  final_outcome TEXT NULL,
  error_code TEXT NULL,
  error_message TEXT NULL,
  input_artifact_key TEXT NULL
);

CREATE INDEX runs_request_hash_idx ON runs(request_hash);

CREATE TABLE steps (
  step_id UUID PRIMARY KEY,
  run_id UUID NOT NULL REFERENCES runs(run_id),
  step_name TEXT NOT NULL,
  attempt INT NOT NULL DEFAULT 1,
  started_at TIMESTAMPTZ NOT NULL,
  finished_at TIMESTAMPTZ NULL,
  status TEXT NOT NULL,
  input_hash CHAR(64) NOT NULL,
  output_hash CHAR(64) NULL,
  artifact_key TEXT NULL,
  error_code TEXT NULL,
  error_message TEXT NULL
);

CREATE INDEX steps_run_step_attempt_idx ON steps(run_id, step_name, attempt);

CREATE TABLE artifacts (
  artifact_id UUID PRIMARY KEY,
  run_id UUID NOT NULL REFERENCES runs(run_id),
  step_name TEXT NOT NULL,
  artifact_type TEXT NOT NULL,
  storage_key TEXT NOT NULL,
  sha256 CHAR(64) NOT NULL,
  bytes BIGINT NOT NULL,
  created_at TIMESTAMPTZ NOT NULL
);

CREATE INDEX artifacts_run_step_idx ON artifacts(run_id, step_name);
CREATE INDEX artifacts_run_type_idx ON artifacts(run_id, artifact_type);

CREATE TABLE audit_log (
  audit_id UUID PRIMARY KEY,
  run_id UUID NULL REFERENCES runs(run_id),
  ts TIMESTAMPTZ NOT NULL,
  actor_type TEXT NOT NULL,
  actor_id TEXT NULL,
  event_type TEXT NOT NULL,
  event_payload_key TEXT NULL,
  event_payload_small JSONB NULL
);

CREATE INDEX audit_run_ts_idx ON audit_log(run_id, ts);
CREATE INDEX audit_event_ts_idx ON audit_log(event_type, ts);
