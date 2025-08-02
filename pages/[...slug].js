import Link from 'next/link';
import { getAllPageSlugs, getPage } from '../lib/content';

export default function Page({ title, contentHtml }) {
  return (
    <main>
      <h1>{title}</h1>
      <div dangerouslySetInnerHTML={{ __html: contentHtml }} />
      <p><Link href="/">トップへ戻る</Link></p>
    </main>
  );
}

export async function getStaticPaths() {
  const paths = getAllPageSlugs();
  return { paths, fallback: false };
}

export async function getStaticProps({ params }) {
  const slugArray = params.slug;
  const page = await getPage(slugArray);
  return { props: page };
}
