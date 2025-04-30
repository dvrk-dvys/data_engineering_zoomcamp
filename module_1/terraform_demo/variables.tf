variable "credentials" {
  description = "GC Creds"
  default     = "./keys/my_creds.json"
}

variable "project_id" {
  description = "Google Cloud Project"
  default     = "taxi-rides-ny-457909"
}

variable "region" {
  description = "Project region"
  default     = "europe-west3"
}

variable "location" {
  description = "Project location"
  default     = "EU"
}

variable "gc_bucket_name" {
  description = "bucket name if not randomly generate using local"
  default     = "terraform-demo-397122-terra-bucket"
  #default = ""
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  default     = "demo_dataset"
}

variable "gc_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}

variable "table_name" {
  description = "default fact table"
  default     = "taxi_fact_table"
}

variable "schema" {
  description = "Schema for the table"
  default     = "./schema.json"
}