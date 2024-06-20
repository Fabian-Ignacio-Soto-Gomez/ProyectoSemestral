import { useNavigate } from "react-router-dom";
import { useState } from "react";
import { getSHA256Hash } from "boring-webcrypto-sha256";
import { useTranslation } from "react-i18next";

export function CreateAccountForm() {
  const navigate = useNavigate();
  const { t } = useTranslation();
  const [userName, SetUserName] = useState("");
  const [userLastName, SetUserLastName] = useState("");
  const [userEmail, SetUserEmail] = useState("");
  const [userPassword, SetUserPassword] = useState("");
  const [userConfirmPassword, SetUserConfirmPassword] = useState("");

  async function handleCreateForm() {
    // Validate password with confirmPassword

    // Encrypted in sha256
    const hashPasword = await getSHA256Hash(userPassword);
    console.log(hashPasword);

    // Navigation
    navigate("/home");
  }

  return (
    <div className="my-10 shadow-lg max-w-md mx-auto bg-slate-50 p-4 rounded-lg">
      <form className="p-5">
        <div className="space-y-6">
          <div>
            <p className="text-2xl">{t("CreateAccount.title")}</p>
          </div>
          <div>
            <label className="block mb-1">{t("CreateAccount.name")}</label>
            <input
              type="text"
              id="UserName"
              className="w-full p-2 rounded border border-solid border-slate-200"
              placeholder={t("CreateAccount.name")}
              onChange={(e) => SetUserName(e.target.value)}
              value={userName}
              required
            />
          </div>
          <div>
            <label className="block mb-1">{t("CreateAccount.lastname")}</label>
            <input
              type="text"
              id="UserLastName"
              className="w-full p-2 rounded border border-solid border-slate-200"
              placeholder={t("CreateAccount.lastname")}
              onChange={(e) => SetUserLastName(e.target.value)}
              value={userLastName}
              required
            />
          </div>
          <div>
            <label className="block mb-1">{t("CreateAccount.email")}</label>
            <input
              type="email"
              id="UserEmail"
              className="w-full p-2 rounded border border-solid border-slate-200"
              placeholder={t("CreateAccount.email")}
              onChange={(e) => SetUserEmail(e.target.value)}
              value={userEmail}
              required
            />
          </div>
          <div>
            <label className="block mb-1">{t("CreateAccount.password")}</label>
            <input
              type="password"
              id="UserPassword"
              className="w-full p-2 rounded border border-solid border-slate-200"
              placeholder={t("CreateAccount.password")}
              onChange={(e) => SetUserPassword(e.target.value)}
              value={userPassword}
              required
            />
          </div>
          <div>
            <label className="block mb-1">{t("CreateAccount.confirmpassword")}</label>
            <input
              type="password"
              id="UserPassword"
              className="w-full p-2 rounded border border-solid border-slate-200"
              placeholder={t("CreateAccount.confirmpassword")}
              onChange={(e) => SetUserConfirmPassword(e.target.value)}
              value={userConfirmPassword}
              required
            />
          </div>
        </div>
        <div className="mt-6 flex justify-end">
          <button
            type="submit"
            className="rounded-md bg-green-600 px-4 py-2 text-sm font-semibold text-white shadow-sm hover:bg-green-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-green-600"
            onClick={(e) => {
              e.preventDefault();
              handleCreateForm();
            }}
          >
            {t("CreateAccount.btn-form")}
          </button>
        </div>
      </form>
    </div>
  );
}
