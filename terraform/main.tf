provider "google" {
  credentials = "${file(var.service-account-file)}"
  project     = "bench-200118"
  region      = "asia-south1"
}