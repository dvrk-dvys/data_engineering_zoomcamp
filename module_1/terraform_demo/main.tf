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
  # credentials = "./keys/my_creds.json"
  project = "taxi-rides-ny-457909"
  region  = "europe-west3"
}

resource "random_id" "bucket_id" {
  byte_length = 4
}

resource "google_storage_bucket" "auto-expire" {
  name          = "auto-expiring-bucket-${random_id.bucket_id.hex}"
  location      = "europe-west3"
  force_destroy = true

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


#❯ gcloud default auth-login                                                  ─╯
#OR
#❯ export GOOGLE_CREDENTIALS='/Users/jordanharris/Code/data_engineering_zoomcamp/module_1/terraform_demo/keys/my_creds.json'