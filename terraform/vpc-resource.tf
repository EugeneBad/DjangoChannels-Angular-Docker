resource "google_compute_network" "djchangular-vpc" {
  name                    = "djchangular-vpc"
  auto_create_subnetworks = "false"
  description = "The main vpc for the project"
}