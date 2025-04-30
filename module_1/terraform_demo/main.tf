terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "6.31.0"
    }
  }
}

provider "google" {
  # Configuration options
  credentials = file(var.credentials)
  project     = var.project_id
  region      = var.region
}

resource "random_id" "bucket_id" {
  byte_length = 4
}

locals {
  final_bucket_name = var.gc_bucket_name != "" ? var.gc_bucket_name : "auto-expiring-bucket-${random_id.bucket_id.hex}"
}

resource "google_storage_bucket" "auto-expire" {
  name = local.final_bucket_name
  #name          = var.gc_bucket_name
  #default = "auto-expiring-bucket-${random_id.bucket_id.hex}"

  location      = var.location
  force_destroy = true
  storage_class = var.gc_storage_class

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "Delete"
    }
  }

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}


resource "google_bigquery_dataset" "demo_dataset" {
  dataset_id = var.bq_dataset_name
  location   = var.location
}

resource "google_bigquery_table" "my_table" {
  #dataset_id = var.bq_dataset_name
  dataset_id = google_bigquery_dataset.demo_dataset.dataset_id  # 👈 forces dependency and waits until its created
  table_id   = var.table_name

  schema              = file(var.schema) # schema defined in JSON format
  deletion_protection = false
}



#❯ gcloud default auth-login                                                  ─╯
#OR
#❯ export GOOGLE_CREDENTIALS='/Users/jordanharris/Code/data_engineering_zoomcamp/module_1/terraform_demo/keys/my_creds.json'