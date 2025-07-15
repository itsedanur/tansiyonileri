import argparse, sys
from tsyn import data_loader, preprocessing, model

def main(argv=None):
    parser = argparse.ArgumentParser(description="TSYN: Tansiyon Analizi")
    parser.add_argument("-i", "--input", default="tansiyon.xlsx",
                        help="Girdi Excel dosyası")
    parser.add_argument("-o", "--output", default=None,
                        help="Sonuç dosyası (opsiyonel)")
    args = parser.parse_args(argv)

    df = data_loader.load_excel(args.input)
    df = df.join(preprocessing.split_bp(df["Sabah Tansiyon"]).add_prefix("sabah_"))
    df = df.join(preprocessing.split_bp(df["Akşam Tansiyon"]).add_prefix("aksam_"))

    features = df[["sabah_sistolik","sabah_diyastolik","aksam_sistolik","aksam_diyastolik"]].dropna()
    bp_model = model.BPClusterModel()
    labeled, _ = bp_model.fit_predict(features)
    df = df.join(labeled["risk"])
    print(df[["Tarih","risk"]])
    print("Genel:", model.BPClusterModel.global_risk(df["risk"]))

    if args.output:
        df.to_excel(args.output, index=False)
        print(f"Excel'e kaydedildi ➜ {args.output}")

if __name__ == "__main__":
    main()
