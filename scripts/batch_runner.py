from batch_sher_scraper import run_all_batches

all_batches = [
    {
        "Ameer Minai": "https://www.rekhta.org/poets/ameer-minai/all-shayari",
        "Mir Taqi Mir": "https://www.rekhta.org/poets/mir-taqi-mir/all-shayari"
    },
    {
        "Jigar Moradabadi": "https://www.rekhta.org/poets/jigar-moradabadi/all-shayari",
        "Hasrat Mohani": "https://www.rekhta.org/poets/hasrat-mohani/all-shayari"
    }
]

run_all_batches(all_batches)